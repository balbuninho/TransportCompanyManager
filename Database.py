import sqlite3
import os


class DataBase:

    @staticmethod
    def create_database():
        print('Database file not found...')
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute("""CREATE TABLE vehicle (
                     p_ID,
                     name text,
                     load integer,
                     capacitance integer,
                     driver_1 integer,
                     driver_2 integer,
                     driver_3 integer,
                     status text,
                     number_of_courses integer  
        )""")

        c.execute("""CREATE TABLE employee (
                    p_ID INTEGER NOT NULL,
                    name text,
                    surname text
        )""")

        c.execute("""CREATE TABLE company (
                    number_of_vehicles integer,
                    number_of_drivers integer)
        """)
        conn.commit()
        conn.close()
        print('Database has been created')


def run():  # check if database file already exist if not it will create one using method from class DataBase

    if os.path.exists('Data_base'):
        print('Data Base Found')
    else:
        DataBase.create_database()


if __name__ == "__main__":
    run()
