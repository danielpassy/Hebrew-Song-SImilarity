import psycopg2
import psycopg2.extras
from Processing.database_queries import *


class connect_database():

    def __init__(self):
        self.db = "songSimmilarities"
        self.connect = self.connect_database()
        self.table = "songs"

    def __del__(self):
        if self.connect:
            self.connect.close()

    def change_table(self, table):
        self.table = table

    def connect_database(self):
        f = open('../password.txt', 'r')
        password = f.read()
        connection = psycopg2.connect(
            host='localhost',
            database="songsSimmilarities",
            user='postgres',
            password=password)
        return connection

    def check_in_database(self, dictionary):

        dictionary_cleaned = []
        cursor = self.connect.cursor()
        for i in range(0, len(dictionary)):
            try:
                save = generate_check_query(self.table, dictionary[i]['title'][0], dictionary[i]['author'][0])

                ## to catch entries without artist name. Decided to drop the ones without title and author.
            except IndexError:
                if not (dictionary[i]['title'][0]):
                    break
                else:
                    save = generate_check_query(self.table, dictionary[i]['title'][0], 'UNKNOWN')
                    dictionary[i]['author'].append('UNKNOWN')
            cursor.execute(save)
            if not (cursor.fetchone()):
                dictionary_cleaned.append(dictionary[i])
        cursor.close()

        return dictionary_cleaned


    def load_files(self, n):

        cursor = self.connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = SQL("""SELECT * FROM {} WHERE added = false LIMIT {}""".format(self.table, n))
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

        return data

    def save_file_alternative(self, data):
        cursor = self.connect.cursor()
        for i in range(0, len(data)):
                cursor.execute(organize_file_db1(data[i]))
        self.connect.commit()
        print('salvo de maneira bem sucedida')
        cursor.close()

    def save_file(self, data):

        cursor = self.connect.cursor()
        for i in range(0, len(data)):
            for j in range(0, len(data[i][1])):
                cursor.execute(organize_file_db1(data, i, j, table=self.table))
        self.connect.commit()
        print('salvo de maneira bem sucedida')
        cursor.close()
