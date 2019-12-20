import mysql.connector

mydb= mysql.connector.connect(
	host='139.59.15.45',
	user='admin',
	passwd='0a1fe51d9af7e094ad1d23e50a37a7049a37ae5e99573e3a',
	database='worksheet',
	)
mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')
# mycursor.execute('ALTER TABLE customers ADD COLUMN phone_number INT')

sql='SELECT * FROM server_configs'
# val=('john doe', 'Highway 21','8891021061')
mycursor.execute(sql)

myresult=mycursor.fetchall()
# print(myresult)
for x in myresult:
	print(x)
