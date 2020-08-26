## take entries from DB, tokenize then, turn then into txt
#                   and lemmatize then


from nlp_module.bash_to_YAP import *
import string
import os.path
import json
import sys

## path to the current folder
sys.path.append('C:/Users/Daniel/PycharmProjects/songsSimmilaritiesPython/Processing')
import Processing.database_operations

def load_paths():
    #open the paths in the paths file.

    with open('paths.json') as jsonfile:
        paths = json.load(jsonfile)
    return paths

def tokenize(data):
    #break the lyrics into 1 word per line (tokenize)

    for rows in range(0, len(data)):
        data[rows]['lyrics'] = data[rows]['lyrics'].translate(str.maketrans('', '', string.punctuation))
        data[rows]['lyrics'] = data[rows]['lyrics'].split()
    return data

def song_txt_list_generator(data):
    ## generate the .txt required by the NLP MODULE (yap)

    lista = []
    for rows in data:
        output_file = rows['original_artist'] + "_" + rows['original_song']
        output_file = output_file.replace(" ", "")
        if (output_file == ''):
            print(rows)
        output_path = os.path.join(paths['inputlyrics'], output_file)
        try:
            with open(output_path, 'x+', newline='\n', encoding="utf-8") as f:
                for word in rows['lyrics']:
                    f.write(word)
                    f.write('\n')
                f.write('\n')
        except OSError:
            pass
        lista.append(output_file)

    return lista



def checkif_already_lemmatized(lista):
    #check if the music was already lemmatizied

    cleaned_list = []
    for i in lista:
        file_name = i + ".lattice"
        if (os.path.exists(os.path.join(paths['outputlattice'], file_name))) == False:
            cleaned_list.append(i)
    return cleaned_list



paths = load_paths()
database = Processing.database_operations.connect_database()
data = database.load_files(1250)
data = tokenize(data)
lista = song_txt_list_generator(data)
lista = checkif_already_lemmatized(lista)
f = 0
for i in lista:
    ##  call the NLP module through a script
    callps1(gen_command(i))
    print(f)
    f += 1

