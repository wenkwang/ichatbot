import sqlite3
from common import *


DB_CONNECTION = sqlite3.connect("resource/ichatbot.db")
DB_CURSOR = DB_CONNECTION.cursor()


def get_word_count(word):
    sql_word_count = "SELECT count FROM word WHERE word =:word"
    DB_CURSOR.execute(sql_word_count, {"word": word})
    res_row = DB_CURSOR.fetchone()
    count = res_row[0]
    return count


def find_chat_response(text, category, nouns_str, sentiment):
    if type == "greeting":
        sql_chat_response = "SELECT response1, response2, response3 " \
                            "FROM greeting " \
                            "WHERE nouns =:nouns_str"
    elif type == "question":
        sql_chat_response = "SELECT response1, response2, response3 " \
                            "FROM question " \
                            "WHERE nouns =:nouns_str"
    elif type == "statement":
        sql_chat_response = "SELECT response1, response2, response3 " \
                            "FROM statement " \
                            "WHERE nouns =:nouns_str"
    DB_CURSOR.execute(sql_chat_response, {"nouns_str": nouns_str})
    responses = DB_CURSOR.fetchone()
    if responses is None:
        response = DEFAULT_RESPONSE
        train_achieve_message(text, category, nouns_str)
        return response
    if sentiment < -0.3:
        response = responses[0]
    elif sentiment < 0.3:
        response = responses[1]
    else:
        response = responses[2]
    return response


def train_achieve_message(text, category, nouns_str):
    sql_train_insert = "INSERT INTO train(text, nouns, category) " \
                       "VALUES (?, ?, ?)"
    values = (text, nouns_str, category)
    DB_CURSOR.execute(sql_train_insert, values)
    DB_CONNECTION.commit()


def create_tables():
    sql_greeting_table = "CREATE TABLE greeting (" \
                         "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                         "nouns text, " \
                         "response1 text, " \
                         "response2 text, " \
                         "response3 text)"
    sql_question_table = "CREATE TABLE question (" \
                         "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                         "nouns text, " \
                         "response1 text, " \
                         "response2 text, " \
                         "response3 text)"
    sql_statement_table = "CREATE TABLE statement (" \
                          "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                          "nouns text, " \
                          "response1 text, " \
                          "response2 text, " \
                          "response3 text)"
    sql_word_table = "CREATE TABLE word (" \
                     "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                     "word text, " \
                     "count INTEGER)"
    sql_train_table = "CREATE TABLE train (" \
                      "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                      "text text, " \
                      "nouns text, " \
                      "category text)"
    DB_CURSOR.execute(sql_greeting_table)
    DB_CURSOR.execute(sql_question_table)
    DB_CURSOR.execute(sql_statement_table)
    DB_CURSOR.execute(sql_word_table)
    DB_CURSOR.execute(sql_train_table)
    DB_CONNECTION.commit()

