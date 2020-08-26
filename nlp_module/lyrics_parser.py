#########       extract the lyrics from the lattice file.
#########       compare the songs
#########       upload to the DB


from os import walk
import os.path
from sys import path

## path to the current folder
path.append('C:/Users/Daniel/PycharmProjects/songsSimmilaritiesPython/Processing')
import Processing.database_operations
import json


## every path is identifye in a unified location
def load_paths():
    with open('paths.json') as jsonfile:
        paths = json.load(jsonfile)
    return paths


## get all files that are trnasformed into lattices
def get_file_names(paths):
    f = []
    for (dirpath, dirnames, filenames) in walk(paths['outputlattice']):
        f.extend(filenames)
        break
    return f

def open_file(i, path, mode = 'rt'):
    ## get only the name, removing the extension of the file
    ## return false if file already exist


    try:
        ## try to split the file into .latice and the file name
        print(i)
        i, _ = i.split(".")
        if (os.path.exists(os.path.join(paths['outputlattice'], i))) == False:
            f_original = open(os.path.join(path, i), mode, encoding='utf-8')
            return f_original
        return False
    except ValueError:
        ## try to split in multiple and get only the first
        i = i.split(".")
        if (os.path.exists(os.path.join(paths['outputlattice'], i[0]))) == False:
            f_original = open(os.path.join(path, i[0]), mode, encoding='utf-8')
            return f_original
        return False




def lemmas_into_lyrics(files):
    for i in files:

        ## check if the lemma file exist, if so, process it, if not, skip to the next
        try:
            with open(os.path.join(paths['outputlattice'], i), "rt", encoding='utf-8') as f_input:

                ## check if the file has been processed, if so, skip to the next in list
                f_output = open_file(i, paths['outputlyrics'], 'w')
                if f_output == False:
                    continue

                    ## lets get just the lemmas, and get rid of duplicated . The lemmas are [3]
                file_content = f_input.read().splitlines()
                lines_just_lemmas = []
                for i in file_content[:-1]:
                    a = i.split() #split each line
                    lines_just_lemmas.append(a[3])
                lines_just_lemmas = list(set(lines_just_lemmas))
                for i in lines_just_lemmas:
                    f_output.write(i + '\n')
                f_output.close()



        except FileNotFoundError:
            print("Missing .lattice file")
            continue


def compare_songs(song_list):
    ## loop through all songs, and compare to all songs, except thenselves
    w = [0, 0]

    data = [] ## container that's going to be returned to the function
    for original in song_list:
        w[0] += 1

        ## remove .lattice of the file name and open the lyrics
        f_original = open_file(original, paths['outputlyrics'])
        if f_original == False:
            continue
        f_original = f_original.read().splitlines()

        for compared in song_list:

            ## remove .lattice of the file name and open the lyrics
            f_compared = open_file(compared, paths['outputlyrics'])
            if f_compared == False:
                continue

            # lets check if the counter is equal to the amount of words
            if original == compared:
                continue
            w[1] += 1
            ## open the lyrics and dump then into a list
            f_compared = f_compared.read().splitlines()
            ## count the amount of words of shared words
            counter = 0
            counter_total_words = 0

            for i in f_original:
                counter_total_words += 1
                if i in f_compared:
                    counter += 1



            ## container for the data that we`re going to send to the database
            song_data = {}
            song_data['original_song_key'] = original
            song_data['compared_song_key'] = compared
            song_data['amount_of_lemmas'] = counter_total_words
            song_data['common_lemmas'] = counter
            song_data['percentage'] = counter/counter_total_words

            data.append(song_data)

    return data



paths = load_paths()
file_names = get_file_names(paths)
lemmas_into_lyrics(file_names)
database = Processing.database_operations.connect_database()
data = compare_songs(file_names)
database.change_table("results")
database.save_file_alternative(data)