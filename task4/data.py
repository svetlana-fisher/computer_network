import psycopg2


def write_data(data):
    with psycopg2.connect(
        dbname="myapp_db",
        user="myapp_user",
        password="mypassword",
        host="localhost",
        port="5432"
    ) as connect:
        with connect.cursor() as cursor:
            cursor.executemany('''INSERT INTO habr (authors_name, published_time,
                                   articles_title, publication_hubs) VALUES (%s, %s, %s, %s)''', data)
            connect.commit()

def read_data():
    with psycopg2.connect(
            dbname="myapp_db",
            user="myapp_user",
            password="mypassword",
            host="localhost",
            port="5432"
    ) as connect:
        with connect.cursor() as cursor:
            cursor.execute("SELECT * FROM habr")
            data = cursor.fetchall()
    return data
