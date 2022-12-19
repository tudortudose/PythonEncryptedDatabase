import mysql.connector

HOST_STRING = "localhost"
USER_STRING = "root"
PASSWORD_STRING = "root"
DATABASE_STRING = "encrypted_database"
DATABASE_INSTANCE = None


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


def get_database():
    global DATABASE_INSTANCE
    if DATABASE_INSTANCE is None:
        DATABASE_INSTANCE = connect(HOST_STRING, USER_STRING, PASSWORD_STRING, DATABASE_STRING)
    return DATABASE_INSTANCE
