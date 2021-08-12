import pymysql,pickle
con = pymysql.connect(host="localhost",user="root",password="")
cursor = con.cursor()



with open("all_students_presenty_status.pickle",'rb') as f:
	all_students_presenty_status = pickle.load(f)

try:
	query = "create database AttendanceDB"
	cursor.execute(query)
	print("database created")
except pymysql.err.ProgrammingError as e:
	cursor.execute("use AttendanceDB")
	print("database changed")
	try:
		cursor.execute("create table status(Roll_Number int (5) primary key, Student_Name varchar (50), Status varchar(10))")
		print("table created")
	except pymysql.err.InternalError as e:
		query = "insert into status(Roll_Number,Student_Name,Status) VALUES(%s,%s,%s);"
		records = all_students_presenty_status
		cursor.executemany(query,records)
		con.commit()
		print("records inserted in database")

finally :
	if cursor:
		cursor.close()
	if con:
		con.close()



