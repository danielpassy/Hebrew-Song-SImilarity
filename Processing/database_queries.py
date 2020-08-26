from psycopg2.sql import SQL


def remove_shit_from_string(str):
    ## there is problems with abbreviate words that use '', we end up spliting the string later on
    str = str.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-").replace("\r\n", " ")
    return str


def generate_save_query(table, *args, **kwargs):
    str = ''
    for i in args:
        str += "'" + i + "'" + ", "
    str = str[:-2]
    save = SQL(
        """INSERT INTO {} VALUES({}, {}, {}, {})""".format(table, str, kwargs['amount_of_lemmas'],
                                                             kwargs['common_lemas'], kwargs['percentage']))

    print(save)
    return save


def generate_save_query_legacy(db, lyrics, *args):
    str = ''
    for i in args:
        str += "'" + i + "'" + ", "
    str = str[:-2]
    save = SQL("""INSERT INTO {} VALUES({}, false, '{}')""".format(db, str, lyrics))

    print(save)
    return save


def generate_check_query(db, original_song, original_artist):
    original_song = remove_shit_from_string(original_song)
    original_artist = remove_shit_from_string(original_artist)
    save = SQL("""SELECT * FROM {} WHERE original_song = '{}' AND original_artist = '{}'""".format(db, original_song,
                                                                                                   original_artist))
    print(save)
    return save


def generate_database_query_db1(original_song, original_artist, original_url, original_lyrics):
    # removing scape characters
    original_song = remove_shit_from_string(original_song)
    original_artist = remove_shit_from_string(original_artist)
    original_url = remove_shit_from_string(original_url)
    lyrics = ''
    for i in original_lyrics:
        lyrics += i
    lyrics = remove_shit_from_string(lyrics)
    save = generate_save_query_legacy('songs', lyrics, original_song, original_artist, original_url)
    return save


def organize_file_db1(data, table="results"):
    data['original_song_key'] = remove_shit_from_string(data['original_song_key'])
    data['compared_song_key'] = remove_shit_from_string(data['compared_song_key'])

    SQL_COMMAND = generate_save_query(table, data['original_song_key'], data['compared_song_key'],
                                      common_lemas=data['common_lemmas'],
                                      amount_of_lemmas=data['amount_of_lemmas'], percentage=data['percentage'])
    return SQL_COMMAND


def organize_file_db2(data):
    generate_save_query_legacy()


def organize_file_db2_legacy(save, i, j):
    original_song = save[i][0]['title'][0]
    original_artist = save[i][0]['author'][0]
    original_url = save[i][0]['url']
    compared_song = save[i][1][j]['title'][0]
    compared_artist = save[i][1][j]['author'][0]
    compared_url = save[i][1][j]['url']
    words_in_common = save[i][2][j][0]
    total_words = save[i][2][j][1]
    percentage = save[i][2][j][2]

    original_song = original_song.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-")
    original_artist = original_artist.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-")
    original_url = original_url.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-")
    compared_song = compared_song.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-")
    compared_artist = compared_artist.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-")
    compared_url = compared_url.replace("\'", "\'\'").replace("\"", "\'\'").replace("--", "-")

    SQL_COMMAND = generate_save_query_legacy('song_simmilarity', original_song, original_artist, original_url,
                                             compared_song,
                                             compared_artist,
                                             compared_url, words_in_common, total_words, percentage)
    return SQL_COMMAND


print(remove_shit_from_string("נראינו כמו זוג מג'ורנל"))
