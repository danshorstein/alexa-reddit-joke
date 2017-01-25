from tinydb import TinyDB
import os


def open_jokes_database():
    main_directory = os.path.abspath(os.path.dirname(__file__))
    database_directory = 'db'
    jokesdb_path = os.path.join(main_directory, database_directory, 'jokesdb.json')
    return TinyDB(jokesdb_path)