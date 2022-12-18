import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "root"
DATABASE = "encrypted_database"


def connect(host, user, password, database):
    database = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return database


db = connect(HOST, USER, PASSWORD, DATABASE)
