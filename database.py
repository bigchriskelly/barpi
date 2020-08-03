#!/usr/bin/python
#--------------------------------------
#
#
#
#
#--------------------------------------
def update_temp(sensor_index, temp):
    import mysql.connector
    
    mydb = connect_db()

    mycursor = mydb.cursor()

    sql = "INSERT INTO measurements (keg, temp, time) VALUES (" + str(sensor_index + 1) + ", " + str(temp)  + ", now())"
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def connect_db():
    import mysql.connector
    mydb = mysql.connector.connect(       
        host="localhost",
        user="root",
        password="monday",
        database="ratarsedberrypi"
    )
    return mydb

def get_goalTemp():
    import mysql.connector
    
    mydb = connect_db()

    mycursor - mydb.cursor()

    sql = "SELECT goalTemp from keg where active = 1"
    mycursor.execute(sql)
    return mycursor
#def update_weight():
