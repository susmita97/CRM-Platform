import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="susmita",
  passwd="susmita12"
)



mycursor = conn.cursor()

#mycursor.execute()
