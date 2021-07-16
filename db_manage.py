import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE, connect

try:
    db_con = sqlite3.connect('C:\Motorsport\Python\WebScrapping\DB\DBf2.db')
    cursor = db_con.cursor()
    print("Database created and Successfully Connected to SQLite")

    #sqlite_select_Query = "select sqlite_version();"
    #cursor.execute(sqlite_select_Query)
    #record = cursor.fetchall()
    #print("SQLite Database Version is: ", record)
    
    #sql_create_f2_table = ''' CREATE TABLE IF NOT EXISTS f2_cars(car_num integer PRIMARY KEY, driver_short_name text NOT NULL, driver_long_name text);'''
    #cursor.execute(sql_create_f2_table)
    #print("table is created")   

    sql_populate_db = '''INSERT INTO f2_cars(car_num, driver_short_name, driver_long_text) VALUES (4, "DRU", "F.DRUGOVICH"), (5, "TIC", "D.TICKTUM");''' 
    cursor.execute(sql_populate_db)
    db_con.commit()
    
    sql_request = 'SELECT * FROM f2_cars'
    sql_result = cursor.execute(sql_request)
    sql_list = sql_result.fetchall()
    for row in sql_list:
        print(row)
    

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if db_con:
        db_con.close()
        print("The SQLite connection is closed")

