"""
This module handles the database (MySQL) connection & communication:
-singleton connection;
-select, insert, delete statements;
"""

import mysql.connector

HOST_STRING = "localhost"
USER_STRING = "root"
PASSWORD_STRING = "root"
DATABASE_STRING = "encrypted_database"
DATABASE_INSTANCE = None


def connect(host, user, password, database):
    """
    Connects to the database;

    :param host: the host for the database;
    :param user: the user of the database;
    :param password: the password for the given user;
    :param database: the database name;
    :return: a MySql connection object;
    """
    database = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return database


def create_files_table(database):
    """
    Creates a new table in the database (files);
    (Run only once);

    :param database: the database connection object;
    :return: None.
    """
    cursor = database.cursor()
    cursor.execute(
        'CREATE TABLE files(id INT AUTO_INCREMENT PRIMARY KEY, '
        'name VARCHAR(255) NOT NULL UNIQUE, location VARCHAR(255) NOT NULL UNIQUE ,'
        ' encryption_alg VARCHAR(255) NOT NULL , key_size INT NOT NULL )')


def insert_file(database, file_info):
    """
    Inserts a new entry in the "files" table;

    :param database: the database connection object;
    :param file_info: entry data to be inserted;
    :return: None.
    """
    cursor = database.cursor()

    sql_statement = 'INSERT INTO files (name, location, encryption_alg, key_size) ' \
                    'VALUES(%s, %s, %s, %s)'
    sql_values = (file_info["name"], file_info["location"],
                  file_info["encryption_alg"], file_info["key_size"])

    cursor.execute(sql_statement, sql_values)
    database.commit()


def get_file_by_name(database, file_name):
    """
    Retrieves an entry with the given name from the "files" table;

    :param database: the database connection object;
    :param file_name: the name of the file entry;
    :return: the file entry found.
    """
    cursor = database.cursor()
    sql_statement = "SELECT * FROM files WHERE name = %s"
    sql_values = (file_name,)

    cursor.execute(sql_statement, sql_values)
    result = cursor.fetchall()
    return result


def file_name_exists(database, file_name):
    """
    Checks if a file with a given name exists in the database;

    :param database: the database connection object;
    :param file_name: the name of the file entry;
    :return: True, if the searched file exists, False otherwise.
    """
    result = get_file_by_name(database, file_name)
    return len(result) != 0


def delete_file(database, file_name):
    """
    Deletes an entry from the "files" table;

    :param database: the database connection object;
    :param file_name: the name of the file to be deleted;
    :return: None.
    """
    cursor = database.cursor()
    sql_statement = "DELETE FROM files WHERE name = %s"
    sql_values = (file_name,)

    cursor.execute(sql_statement, sql_values)
    database.commit()


def get_database():
    """
    Retrieves one instance of the database;
    (Singleton pattern simulation);

    :return: an instance of the database connection object.
    """
    global DATABASE_INSTANCE
    if DATABASE_INSTANCE is None:
        DATABASE_INSTANCE = connect(HOST_STRING, USER_STRING, PASSWORD_STRING, DATABASE_STRING)
    return DATABASE_INSTANCE
