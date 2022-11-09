import sqlite3
import time

class Database:
    def __init__(self):
        print()
    def inputData(scores):
        with sqlite3.connect('./scorePlayer.db') as db:
            cursor = db.cursor()

            result = time.localtime()
            value = [
                (result.tm_min, scores)
            ]
            cursor.executemany("INSERT INTO players(time, score) VALUES(?, ?)", value)
            #cursor.execute("SELECT * FROM players")
            for data in cursor.execute("SELECT * FROM playerss"):
                print(data)

    def get_checkers_id(subject):
        conn = sqlite3.connect("./scorePlayer.db")
        c = conn.cursor()
        c.execute(f"SELECT id FROM checkers WHERE subject = '{subject}'")
        return c.fetchall()
    def outputData():
        get_checkers_id(score)
