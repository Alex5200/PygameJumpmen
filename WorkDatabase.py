import sqlite3
import time


class Database:
    def __init__(self):
        with sqlite3.connect('DataBase/scorePlayer.db') as db:
            self.Cursos = db.cursor()
            try:
                self.Cursos.execute("CREATE TABLE players(id, time, score)")
            except:
                print("err create dataBase")

    def input_data(self, scores):
        result = time.localtime()
        value = [
            (result.tm_min, scores)
        ]
        self.Cursos.executemany("INSERT INTO players(time, score) VALUES(?, ?)", value)

    def output_data(self):
        self.Cursos.execute(f"SELECT score FROM players")
        arrFatching = []
        fetchAll = self.Cursos.fetchall()
        for el in fetchAll:
            print(el[0])
            arrFatching.append(int(el[0]))
        return sorted(arrFatching, reverse=True)
