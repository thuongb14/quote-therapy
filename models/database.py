import psycopg2

#Reading from the database
def sql_select(query, params = []):
    conn = psycopg2.connect('dbname=quotes')
    cur = conn.cursor()
    cur.execute(query, params)
    return cur.fetchall()

#Writing to the database    
def sql_write(query, params = []):
    conn = psycopg2.connect('dbname=quotes')
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
