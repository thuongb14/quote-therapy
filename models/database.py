import psycopg2

import os

DB_URL = os.environ.get('DATABASE_URL', 'dbname=quotes')

#Reading from the database
def sql_select(query, params = []):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(query, params)
    return cur.fetchall()

#Writing to the database    
def sql_write(query, params = []):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
