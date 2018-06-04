import sqlite3


DB_CONNECTION = sqlite3.connect("ichatbot.db")
DB_CURSOR = DB_CONNECTION.cursor()


def get_word_count(word):
    count = 0
    return count


def find_chat_response(message, type, nouns, sentiment):
    response = ""
    return response