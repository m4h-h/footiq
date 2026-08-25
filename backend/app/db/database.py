import psycopg

DATABASE_URL = "postgresql://yunushussain@localhost/footiq"


def get_connection():
    return psycopg.connect(DATABASE_URL)