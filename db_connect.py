import random
import mysql.connector

DB_USER = ""
DB_PASS = ""

def get_words(how_many):
    cnx = mysql.connector.connect(user=DB_USER, host="127.0.0.1", database="sehantang", password=DB_PASS)
    cur = cnx.cursor()
    cur.execute("select word from words")
    words = random.sample(cur.fetchall(), how_many)
    return words

def add_words(word):
    cnx = mysql.connector.connect(user=DB_USER, host="127.0.0.1", database="sehantang", password=DB_PASS)
    cur = cnx.cursor()
    cur.execute("insert into words (word) values ('%s')"% word)
    cnx.commit()
