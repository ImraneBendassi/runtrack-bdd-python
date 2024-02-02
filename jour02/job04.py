import mysql.connector

mydp = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "imrane13",
    database = "LaPlateforme",
)

cursor = mydp.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

results = cursor.fetchall()
print (results)

cursor.close()

mydp.close()