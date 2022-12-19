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
        'CREATE TABLE files(id INT AUTO_INCREMENT PRIMARY KEY, '
        'name VARCHAR(255) NOT NULL UNIQUE, location VARCHAR(255) NOT NULL UNIQUE ,'
        ' encryption_alg VARCHAR(255) NOT NULL , key_size INT NOT NULL )')


def insert_file(database, file_info):
    cursor = database.cursor()

    sql_statement = 'INSERT INTO files (name, location, encryption_alg, key_size) ' \
                    'VALUES(%s, %s, %s, %s)'
    sql_values = (file_info["name"], file_info["location"],
                  file_info["encryption_alg"], file_info["key_size"])

    cursor.execute(sql_statement, sql_values)
    db.commit()


def get_file_by_name(database, file_name):
    cursor = database.cursor()
    sql_statement = "SELECT * FROM files WHERE name = %s"
    sql_values = (file_name,)

    cursor.execute(sql_statement, sql_values)
    result = cursor.fetchall()
    return result


def file_name_exists(database, file_name):
    result = get_file_by_name(database, file_name)
    return len(result) != 0


def delete_file(database, file_name):
    cursor = database.cursor()
    sql_statement = "DELETE FROM files WHERE name = %s"
    sql_values = (file_name,)

    cursor.execute(sql_statement, sql_values)
    database.commit()


db = connect(HOST, USER, PASSWORD, DATABASE)
insert_file(db,
            {
                "name": "file2",
                "location": "C:/Users/tudor/Desktop/file2.txt",
                "encryption_alg": "RSA",
                "key_size": 1024
            })
print(get_file_by_name(db, "file2"))
delete_file(db, "file2")
