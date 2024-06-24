import psycopg2

def query_data():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="hw02",
            user="postgres",
            password="567234",
            host="localhost"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM websites")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    query_data()
