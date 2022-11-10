import sqlite3
import time


class Database:
    def __init__(self):
        with sqlite3.connect('./scorePlayer.db') as db:
            cursos = db.cursor()
            try:
                cursos.execute("CREATE TABLE players(id, time, score)")
            except:
                print("err create dataBase")

    def inputData(scores):
        with sqlite3.connect('./scorePlayer.db') as db:
            cursor = db.cursor()

            result = time.localtime()
            value = [
                (result.tm_min, scores)
            ]
            cursor.executemany("INSERT INTO players(time, score) VALUES(?, ?)", value)
            # cursor.execute("SELECT * FROM players")
            for data in cursor.execute("SELECT * FROM players"):
                print(data)

    def outputData():
        conn = sqlite3.connect("./scorePlayer.db")
        c = conn.cursor()
        c.execute(f"SELECT score FROM players")
        arrFatching = []
        fetchAll = c.fetchall()
        for el in fetchAll:
            print(el[0])
            arrFatching.append(int(el[0]))
        return sorted(arrFatching, reverse=True)
