import mysql.connector

conn = mysql.connector.connect(host="192.168.1.5",user="navii",passwd="1211",database="ttm")
print(conn)