#!/usr/bin/python3

import os
import sqlite3
import sys


def create_db_table():
    conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
    cursor = conn.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS secrets(email TEXT PRIMARY KEY, secret TEXT); ''')

    conn.commit()


def create_db_record(email, secret_key):
    create_db_table()

    conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
    cursor = conn.cursor()

    cursor.execute(''' INSERT INTO secrets(email, secret) VALUES(?,?) ''', (email, secret_key))

    conn.commit()


def remove_db_record(email):
    conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
    cursor = conn.cursor()

    cursor.execute(''' DELETE FROM secrets WHERE email=? ''', (email,))

    conn.commit()


def check_if_email_exists(email):
    conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
    cursor = conn.cursor()

    result = cursor.execute(''' SELECT * FROM secrets WHERE email=? ''', (email,)).fetchall()

    return len(result)


def check_if_any_record_exists():
    conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
    cursor = conn.cursor()

    result = cursor.execute(''' SELECT COUNT(*) FROM secrets ''').fetchall()[0][0]

    return result


def read_secret_from_db(email):
    try:
        conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
        cursor = conn.cursor()

        cursor.execute(''' SELECT secret FROM secrets WHERE email=? ''', (email,))

        return cursor.fetchall()[0][0]
    except sqlite3.Error as err:
        print(err)
        return None


def list_all_records(with_secrets=False):
    conn = sqlite3.connect(os.environ.get("HOME") + "/mfa.db")
    cursor = conn.cursor()

    if with_secrets:
        result = cursor.execute(''' SELECT * FROM secrets ''').fetchall()
    else:
        result = cursor.execute(''' SELECT email FROM secrets ''').fetchall()

    print(result)
