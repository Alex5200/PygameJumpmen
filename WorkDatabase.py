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
    def outputData():
        with sqlite3.connect('./scorePlayer.db') as db:
            cursor = db.cursor()
            for score in cursor.execute("SELECT MAX(score) FROM playerss"):
                print(score)
                return score
