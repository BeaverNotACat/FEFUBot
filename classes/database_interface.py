import sqlite3

class DatabaseInterface:
    def __init__(self, path_to_database: str):
        self.__connection = sqlite3.connect(path_to_database, check_same_thread=False)
        self.__cursor = self.__connection.cursor()

    def __execute(self, query):
        self.__cursor.execute(query)
        self.__connection.commit()
        return self.__cursor

    def __read(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def create_user(self, user_id: int) -> None:
        return self.__execute(f'''
        INSERT INTO
            users (user_id)
        VALUES
            ({user_id})
        ''')

    def get_user_by_id(self, user_id) -> list:
        return self.__read((f"""SELECT * FROM users WHERE id = {user_id}"""))

    def check_for_delivery_role(self, user_id: int):
        return self.__read(f"""SELECT is_deliveryman FROM users WHERE id = {user_id}""")


