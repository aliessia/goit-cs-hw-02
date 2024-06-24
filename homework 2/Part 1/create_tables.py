import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS websites (
            id SERIAL PRIMARY KEY,
            url VARCHAR(255) NOT NULL,
            status VARCHAR(10) NOT NULL
        )
        """,
    )
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="hw02",
            user="postgres",
            password="567234",
            host="localhost"
        )
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
    print("Tables created successfully")
