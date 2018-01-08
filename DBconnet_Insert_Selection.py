Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pymysql
>>> conn = pymysql.connect(host = 'localhost', user='root', password='1234', db='stockset', charset='utf8')
>>> curs = conn.cursor()
>>> sql = """insert into basic_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
>>> curs.execute(sql,("123461", "Perlabyss", "15500", "15700", "15800", "525000", "528000", "622000", "800000", "420000", "380000"))
1
>>> conn.commit()
>>> print(curs.fetchall)
<bound method Cursor.fetchall of <pymysql.cursors.Cursor object at 0x0000000002B795C0>>
>>> curs.execute('select *from basic_fixed')
6
>>> print(curs.fetchall())
(('123456', 'Samsung', '3310', '3350', '3650', '45000', '48000', '52000', '375000', '250000', '125000'), ('123457', 'LGDISPLAY', '5500', '5700', '5800', '55000', '58000', '62000', '500000', '280000', '220000'), ('123458', 'Hyundai', '500', '700', '800', '5000', '8000', '2000', '5000', '2800', '2200'), ('123459', '나라완', '5500', '5700', '5800', '55000', '58000', '62000', '500000', '280000', '220000'), ('123460', 'Perlabyss', '15500', '15700', '15800', '525000', '528000', '622000', '800000', '420000', '380000'), ('123461', 'Perlabyss', '15500', '15700', '15800', '525000', '528000', '622000', '800000', '420000', '380000'))
>>> curs.execute('select CODE from basic_fixed;')
6
>>> with conn.cursor() as curs:
	sql = "select CODE, DPT from basic_fixed;"
	curs.execute(sql)
	rs = curs.fetchall()
	for row in rs:
		print(row)

		
6
('123456', '125000')
('123457', '220000')
('123458', '2200')
('123459', '220000')
('123460', '380000')
('123461', '380000')
>>> with conn.cursor() as curs:
	sql = "select CODE, DPT from basic_fixed where NIQ2 < 50000;"
	curs.execute(sql)
	rs = curs.fetchall()
	for row in rs:
		print(row)

		
6
('123456', '125000')
('123457', '220000')
('123458', '2200')
('123459', '220000')
('123460', '380000')
('123461', '380000')
>>> with conn.cursor() as curs:
	sql = "select CODE, DPT from basic_fixed where NIQ2 < 5000;"
	curs.execute(sql)
	rs = curs.fetchall()
	for row in rs:
		print(row)

		
2
('123456', '125000')
('123458', '2200')
>>> 
