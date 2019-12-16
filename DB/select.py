import mysql.connector

mydb= mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='primary',
	database='python_db',
	)
mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')
# mycursor.execute('ALTER TABLE customers ADD COLUMN phone_number INT')

sql='SELECT * FROM customers'
val=('john doe', 'Highway 21','8891021061')
mycursor.execute(sql)

myresult=mycursor.fetchall()
print(mycursor)
# for x in myresult
