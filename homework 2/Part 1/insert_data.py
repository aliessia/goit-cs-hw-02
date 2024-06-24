import psycopg2

def insert_data():
    websites = [
        ("https://google.com", "UP"),
        ("https://facebook.com", "UP"),
        ("https://twitter.com", "UP")
    ]
    sql = """INSERT INTO websites(url, status)
             VALUES(%s, %s) ON CONFLICT (url) DO UPDATE SET status = EXCLUDED.status;"""
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="hw02",
            user="postgres",
            password="567234",
            host="localhost"
        )
        cur = conn.cursor()
        cur.executemany(sql, websites)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_data()
    print("Data inserted successfully")
