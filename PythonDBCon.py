import mysql.connector

con = mysql.connector.connect(host='localhost', password='admin', user='root')

if con.is_connected():
    print("Database Connect")
    print("Python Database Connectivity Successfull")
    print("Connection Established.")
    print(con)
