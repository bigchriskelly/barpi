#!/usr/bin/python
#--------------------------------------
#
#
#
#
#--------------------------------------
def get_is_crash():
    mydb = connect_db()
    sql = "SELECT isCrash FROM keg where isCrash is not null order by time desc limit 1"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    records = mycursor.fetchone()
    print(records[0])
    return records[0]


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

def get_goal_temp():
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "SELECT goalTemp from keg where goalTemp is not null order by time desc limit 1"
    mycursor.execute(sql)
    records = mycursor.fetchone()
    return records[0]

def get_wiggle_temp():
    mydb = connect_db()
    mycursor =mydb.cursor()
    sql = "select wiggleTemp from keg where wiggleTemp is not null order by time desc limit 1"
    mycursor.execute(sql)
    records = mycursor.fetchone()
    return records[0]

def get_keg_temp(keg):
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "select temp from measurements where temp is not null and keg = " + str(keg) + " order by time desc limit 1"
    mycursor.execute(sql)
    records = mycursor.fetchone()
    return records[0]

def update_relay_DB(state):
    mydb = connect_db()
    mycursor = mydb.cursor()
    sql = "insert into ratarsedberrypi.relay (time, position) values (now(), " + str(state) + ")"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
