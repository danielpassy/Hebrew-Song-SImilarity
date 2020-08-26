import json
import os
from typing import List, Any

data_path = os.path.join(os.getcwd(), 'data')



def load_data():
    with open('../data/tokenized_11.json') as jsonfile:
        data = json.load(jsonfile)
    return data


def write_json(data):
    version = 0
    try:
        with open('../data/results.json', 'x') as f:
            json.dump(data, f)
    except FileExistsError:
        write_json_attempt(data, version)


def write_json_attempt(data, version):
    try:
        filename = 'data\\'+ 'results' + str(version) + '.json'
        with open(filename, 'x') as f:
            json.dump(data, f)
            f.close()
    except FileExistsError:
        version += 1
        write_json_attempt(data, version)


def compare_exactwords(dictionary):
    # method for getting song comparision metrics
    returnwrapper: List[List[Any]] = [[]]
      # metadata of reference song
    for reference_row in range(0, len(dictionary)):
        print(reference_row)
        referenceSong = dictionary[reference_row]
        comparedSong = []  # metadata of each song
        results = []  # comparision metrics

        for compared_row in range(0, len(dictionary)):
            # get the metrics for each pair of songs, store in Results
            results.append(count_words(dictionary[reference_row]['lyrics'], dictionary[compared_row]['lyrics']))
            comparedSong.append(modified_dict(dictionary[compared_row]))  # append metadata
            # finished compared the first song to all the rest, now include the results in lists and procced with next song

        # lets create the wrapper
        returnwrapper.append([])
        returnwrapper[reference_row].extend([referenceSong, comparedSong, results])
    del (returnwrapper[len(dictionary)])
    return returnwrapper


def count_words(song1, song2):
    common_words = []  # list of shared words
    counter: int = 0  # num of words from song 1 that are also in song 2, including repetitions
    song1_lenght = len(song1)
    for word_song1 in song1:
        if word_song1 in song2:  # if order this way to include words that already appeared on the counter
            counter += 1
            if word_song1 not in common_words:
                common_words.append(word_song1)
    results = []
    results.extend([counter, song1_lenght, counter / song1_lenght])
    return results


def modified_dict(dictionary):
    copy = dict(dictionary)
    del copy["lyrics"]
    return copy



data = load_data()
comparision_wrapper = compare_exactwords(data)
write_json(comparision_wrapper)
