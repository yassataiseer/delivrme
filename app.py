import mysql.connector

db =mysql.connector.connect(
    host = "localhost",
    user = "root" ,
    passwd = "root",
    database = "deliverdatabase"
)
#mycursor = db.cursor()
#mycursor.execute("CREATE TABLE User(Username VARCHAR(50), Password VARCHAR (10), personID int PRIMARY KEY AUTO_INCREMENT)")
#db.commit()
