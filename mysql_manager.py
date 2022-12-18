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


def create_files_table(database):
    cursor = database.cursor()
    cursor.execute(
        'CREATE TABLE files(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL UNIQUE ,'
        ' location VARCHAR(255) NOT NULL UNIQUE , encryption_alg VARCHAR(255) NOT NULL , key_size INT NOT NULL )')


def insert_file(database, file_info):
    cursor = database.cursor()
    sql_statement = 'INSERT INTO files (name, location, encryption_alg, key_size) ' \
                    'VALUES(%s, %s, %s, %s)'
    sql_values = (file_info["name"], file_info["location"],
                  file_info["encryption_alg"], file_info["key_size"])
    print(sql_values)
    cursor.execute(sql_statement, sql_values)
    db.commit()


db = connect(HOST, USER, PASSWORD, DATABASE)
create_files_table(db)
insert_file(db,
            {
                "name": "file1",
                "location": "C:/Users/tudor/Desktop/file1.txt",
                "encryption_alg": "RSA",
                "key_size": 1024
            })
