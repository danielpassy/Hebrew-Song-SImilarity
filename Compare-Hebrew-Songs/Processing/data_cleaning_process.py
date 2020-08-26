##### access the dictionary that was scrapped from the website.
##### clean it, get the lyrics, connect to a database, and upload.


import os
import string
import warnings
import json
from Processing.database_operations import *

data_path = os.path.join(os.getcwd(), 'data')

def load_json_file():
    with open('../data/datatest.json') as jsonfile:
        paths = json.load(jsonfile)
    return paths

def access_modify_outer_row(dictionary, procedure):
    dictionary_cleaned = []
    for rows in range(0, len(data)):
        procedure(dictionary, dictionary_cleaned, rows)
    return dictionary_cleaned


def access_modify_inner_row(dictionary, procedure):
    for rows in range(0, len(dictionary)):
        lyrics = []
        for insiderows in range(0, len(dictionary[rows]['lyrics'])):
            procedure(dictionary, lyrics, rows, insiderows)
        dictionary[rows]['lyrics'] = lyrics
    return dictionary


def append_only_non_empty_entries(dictionary, dictionary_cleaned, rows):
    if (dictionary[rows].get('lyrics')):
        dictionary_cleaned.append(dictionary[rows])


def append_only_hebrew_lyrics(dictionary, dictionary_cleaned, rows):
    if any("\u0590" <= c <= "\u05EA" for c in dictionary[rows]['lyrics']):
        dictionary_cleaned.append(dictionary[rows])


def append_only_non_xao_lines(dictionary, lyrics, rows, insiderows):
    lyrics.append(dictionary[rows]['lyrics'][insiderows].replace('\xa0', ' '))


def append_only_non_empty_lines(dictionary, lyrics, rows, insiderows):
    if not str.isspace(dictionary[rows]['lyrics'][insiderows]):
        lyrics.append(dictionary[rows]['lyrics'][insiderows])

def remove_punctuaction(dictionary, lyrics, rows, insiderows):
    punctuation = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    lyrics.append(dictionary[rows]['lyrics'][insiderows].translate(str.maketrans('', '', string.punctuation)))

warnings.warn("this function need to be teste")


def write_on_database(dictionary):

    ##atempts to connect to the database
    connection = connect_database()
    if (connection == "error"):
        return "error"

    ## actual operation
    cursor = connection.cursor()
    for i in range(0, len(dictionary)):
        save = generate_database_query_db1(dictionary[i]['title'][0], dictionary[i]['author'][0], dictionary[i]['url'], dictionary[i]['lyrics'])
        cursor.execute(save)
    connection.commit()
    print('salvo de maneira bem sucedida')


    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")




data = load_json_file()
data = access_modify_outer_row(data, append_only_non_empty_entries)
data = access_modify_outer_row(data, append_only_hebrew_lyrics)
data = access_modify_inner_row(data, append_only_non_xao_lines)
data = access_modify_inner_row(data, append_only_non_empty_lines)
data = access_modify_inner_row(data, remove_punctuaction)
database = connect_database()
data = database.check_in_database(data)
database.save_file(data)

