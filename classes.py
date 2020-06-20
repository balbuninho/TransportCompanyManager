import sqlite3
import os
import sys
import Database


class Driver:

    @staticmethod
    def get_drivers_list():
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT * FROM employee')
        data = c.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_driver_data():
        new_id = int(input('Enter Drivers ID: '))
        name = input('Enter Drivers name: ')
        surname = input('Enter Drivers surname: ')
        ls = [new_id, name, surname]
        return ls

    @staticmethod
    def check_for_id():
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT MAX(p_ID) FROM employee ')
        value = c.fetchall()
        x = value[0]
        try:
            new = int(x[0])
            return new
        except TypeError:
            return None

    @staticmethod
    def get_data_for_driver_update():
        get_id = int(input('Enter Drivers ID which you want to edit: '))
        name = input('Enter New Drivers name: ')
        surname = input('Enter New Drivers surname: ')
        ls = [get_id, name, surname]
        return ls

    @staticmethod
    def show_number_of_employees():
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM employee')
        x = c.fetchall()[0]
        new = x[0]
        print(new)
        conn.close()

    @staticmethod
    def get_drivers_name():
        name = input('Enter drivers name')
        return name

    @staticmethod
    def get_drivers_surname():
        surname = input('Enter drivers surname')
        return surname

    def get_dr_id(self):
        s = input('Enter drivers ID to assign: ')
        try:
            return int(s)
        except ValueError:
            print('Value Error')
            self.get_dr_id()

    def get_p_id(self):
        try:
            p_id = int(input('Enter vehicle ID: '))
            return p_id
        except ValueError:
            print('Value Error')
            self.get_p_id()

    def get_slots(self):
        p_id = self.get_p_id()

        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT driver_1, driver_2, driver_3 FROM vehicle WHERE p_ID = ?', (p_id, ))

        slots = []

        try:
            for element in c.fetchall():
                slots.append(element)
                conn.close()
                print(p_id, slots)
                return p_id
        except ValueError:
            print(p_id, [])
            conn.close()
            return p_id

    def assign_driver(self):
        p_id = self.get_slots()
        dr_id = self.get_dr_id()
        dr_slot = int(input('Enter slot (1/2/3): '))
        if dr_slot == 1:
            conn = sqlite3.connect('Data_base')
            c = conn.cursor()
            c.execute('UPDATE  vehicle SET driver_1=? WHERE p_ID=?', (dr_id, p_id))
            conn.commit()
            conn.close()
        elif dr_slot == 2:
            conn = sqlite3.connect('Data_base')
            c = conn.cursor()
            c.execute('UPDATE  vehicle SET driver_2=? WHERE p_ID=?', (dr_id, p_id))
            conn.commit()
            conn.close()
        elif dr_slot == 3:
            conn = sqlite3.connect('Data_base')
            c = conn.cursor()
            c.execute('UPDATE  vehicle SET driver_3=? WHERE p_ID=?', (dr_id, p_id))
            conn.commit()
            conn.close()

    def display_assign_driver(self):
        data = self.check_for_free_slot()
        try:
            print('Driver 1', data[0], '\n'
                  'Driver 2', data[1], '\n'
                  'Driver 3', data[2])
            return True, data
        except IndexError:
            return False

    def check_for_free_slot(self):
        p_id = input('Enter vehicle ID: ')
        try:
            int(p_id)
            conn = sqlite3.connect('Data_base')
            c = conn.cursor()
            c.execute('SELECT driver_1, driver_2, driver_3 FROM vehicle WHERE p_ID=?', (p_id, ))
            print(c.fetchall())
            data = c.fetchall()
            conn.close()
            return data, p_id
        except ValueError:
            print('Value Error')
            self.check_for_free_slot()
        except IndexError:
            print('None drivers assigned')
            return 'Null'

    def search_for_driver_by_surname(self):
        data = self.get_drivers_surname()
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT * FROM employee WHERE surname=?', (data, ))
        data = c.fetchall()
        conn.close()
        return data

    def search_for_driver_by_name(self):
        data = self.get_drivers_name()
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT * FROM employee WHERE name=?', (data, ))
        data = c.fetchall()
        conn.close()
        return data

    def add_driver(self):
        current_id = self.check_for_id()
        print('Current highest ID: ', current_id)
        data = self.get_driver_data()
        name = str(data[1])
        surname = str(data[2])
        new_id = str(data[0])
        conn = sqlite3.connect('Data_base')
        conn.execute('INSERT INTO  employee (p_ID, name,surname) VALUES (?,?,?)', (new_id, name, surname))
        conn.commit()
        conn.close()

    def update_drivers_data(self):
        get_data = self.get_data_for_driver_update()
        dr_id = get_data[0]
        name = get_data[1]
        surname = get_data[2]
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('UPDATE employee SET name = ?, surname = ?  WHERE p_ID = ?', (name, surname, dr_id))
        conn.commit()
        conn.close()

    def print_drivers_list(self):
        data = self.get_drivers_list()
        print(data)


class Vehicle:

    @staticmethod
    def get_v_name():
        data = input('Enter vehicle name: ')
        return data

    @staticmethod
    def get_v_load():
        data = input('Enter vehicle load: ')
        return data

    @staticmethod
    def get_v_cap():
        data = input('Enter vehicle capacity: ')
        return data

    @staticmethod
    def check_for_id():
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT MAX(p_ID) FROM vehicle ')
        value = c.fetchall()
        x = value[0]
        try:
            new = int(x[0])
            return new
        except TypeError:
            return None

    @staticmethod
    def show_v_list():
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT * FROM vehicle')
        print(c.fetchall())
        conn.close()

    @staticmethod
    def show_number_of_v():
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM vehicle')
        x = c.fetchall()[0]
        new = x[0]
        print(new)
        conn.close()

    def change_status_out(self):
        get_id = input('Enter vehicle ID: ')
        status = 'OUT'
        try:
            int(get_id)
            conn = sqlite3.connect('Data_base')
            c = conn.cursor()
            c.execute('UPDATE vehicle SET status=? WHERE p_ID =?', (status, get_id))
            conn.commit()
            conn.close()
        except ValueError:
            print('Value Error')
            self.change_status_out()

    def change_status_back(self):
        get_id = input('Enter vehicle ID: ')
        status = 'BACK'
        try:
            int(get_id)
            conn = sqlite3.connect('Data_base')
            c = conn.cursor()
            c.execute('SELECT number_of_courses FROM vehicle WHERE p_ID=?', (get_id,))
            number = int(c.fetchall()[0])
            number += 1
            c.execute('UPDATE vehicle SET status=? number_of_courses=? WHERE p_ID =?', (status, number, get_id))
            conn.commit()
            conn.close()
        except ValueError:
            print('Value Error')
            self.change_status_out()

    def edit_v_data(self):
        get_id = self.get_v_id()
        get_name = self.get_v_name()
        get_cap = self.get_v_cap()
        get_load = self.get_v_load()
        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('UPDATE vehicle SET name=?, load=?, capacitance=? WHERE p_ID = ?', (get_name, get_load, get_cap,
                                                                                      get_id))
        conn.commit()
        conn.close()

    def get_v_id(self):
        current = self.check_for_id()
        print('current highest ID: ', current)
        iid = (input('Enter ID: '))
        nc = int(current)
        try:
            compare_id = int(iid)
            if compare_id == nc or compare_id < nc:
                print('Value Error')
                self.get_v_id()
            else:
                return iid
        except ValueError:
            print('Value Error')
            self.get_v_id()

    def add_vehicle(self):
        p_id = self.get_v_id()
        name = self.get_v_name()
        load = self.get_v_load()
        cap = self.get_v_cap()
        try:
            new_id = int(p_id)

        except ValueError:
            new_id = 1

        conn = sqlite3.connect('Data_base')
        c = conn.cursor()
        c.execute('INSERT INTO vehicle (p_ID,name,load,capacitance) VALUES(?,?,?,?)', (new_id, name, load, cap))
        conn.commit()
        conn.close()
        print('Vehicle added')


class Interface:

    @staticmethod
    def display_menu():
        print(""" 1 = MANAGE TRUCKS:
        1 - Show Trucks List
        2 - Add New Truck 
        3 - Edit Vehicle Data
        4 - Change Truck Status OUT
        5 - Change Truck Status BACK 
        6 - Edit Vehicle Data
        7 - Show Number of Vehicle
2 = MANAGE DRIVERS:
        1 - Show Drivers List
        2 - Add New Driver 
        3 - Edit Driver's Data
        4 - Show Number of Employees
        5 - Assign Driver TO Truck 
3 = EXIT""")

    @staticmethod
    def tak_choose():
        choose = input('SELECT MENU SECTION [1/2/EXIT]: ')
        return choose

    @staticmethod
    def take_choose2():
        choose2 = input('SELECT OPTION: [1-7]: ')
        return choose2


if __name__ == "__main__":

    Database.run()

    while True:

        menu = Interface()
        menu.display_menu()
        c1 = menu.tak_choose()
        ob = Vehicle()
        dr = Driver()

        if c1 == '1':
            c2 = menu.take_choose2()
            if c2 == '1':
                os.system('cls')
                print('Vehicle List')
                ob.show_v_list()
            elif c2 == '2':
                os.system('cls')
                print('Adding Truck...')
                ob.add_vehicle()
            elif c2 == '3':
                os.system('cls')
                print('Edit Vehicle Data...')
                ob.edit_v_data()
            elif c2 == '4':
                os.system('cls')
                print('Change Status to OUT')
                ob.change_status_out()
            elif c2 == '5':
                os.system('cls')
                print('Change Status to BACK')
                ob.change_status_back()
            elif c2 == '6':
                os.system('cls')
                print('Edit Vehicle data...')
                ob.edit_v_data()
            elif c2 == '7':
                os.system('cls')
                ob.show_number_of_v()

        elif c1 == '2':
            c2 = menu.take_choose2()
            if c2 == '1':
                os.system('cls')
                print('V Drivers list V')
                dr.print_drivers_list()

            if c2 == '2':
                os.system('cls')
                print('Adding Driver... ')
                dr.add_driver()
            if c2 == '3':
                os.system('cls')
                print("Edit Driver's data")
            if c2 == '4':
                os.system('cls')
                print('Number of employees')
                dr.show_number_of_employees()
            if c2 == '5':
                os.system('cls')
                print('Assign Driver To Truck')
                dr.assign_driver()
        elif c1 == '3':
            sys.exit()
