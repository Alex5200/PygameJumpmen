import sqlite3
import time


class Database:
    def __init__(self):
        with sqlite3.connect('./DataBase/scorePlayer.db') as db:
            self.Cursos = db.cursor()
            try:
                self.Cursos.execute("CREATE TABLE players(id, time, score, name)")
            except:
                print("null")


    def input_data(self, scores, NAME):
        with sqlite3.connect('./DataBase/scorePlayer.db') as db:
            Cursos = db.cursor()

            result = time.localtime()
            value = [
                (result.tm_min, scores, NAME)
            ]
            print(value)
            Cursos.executemany("INSERT INTO players(time, score, name) VALUES(?, ?, ?)", value)
    def output(self):
        self.Cursos.execute("SELECT MAX(score) FROM players LIMIT 4")
        fetchAll = self.Cursos.fetchall()
        return fetchAll
    def output_max_score_name(self):
        self.Cursos.execute(f"SELECT MAX(score), id, name FROM players")
        fetchAll = self.Cursos.fetchall()
        fetchName = fetchAll[0][2]
        return fetchName

    def output_data(self):
        self.Cursos.execute(f"SELECT score, id, name FROM players")
        array_fatching = []
        fetchAll = self.Cursos.fetchall()
        for el in fetchAll:
            array_fatching.append(int(el[0]))
        sorted_arr = sorted(array_fatching, reverse=True)

        return sorted(array_fatching, reverse=True)


db = Database()
print(db.output())