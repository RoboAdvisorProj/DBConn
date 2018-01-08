Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pymysql
>>> conn = pymysql.connect(host = 'localhost', user='root', password='1234', db='stockset', charset='utf8')
>>> curs = conn.cursor()
>>> sql = """insert into data_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values("123457", "LGDISPLAY", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000")"""
>>> sql = """insert into data_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
>>> curs.execute(sql,("123457", "LGDISPLAY", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000"))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    curs.execute(sql,("123457", "LGDISPLAY", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000"))
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\cursors.py", line 165, in execute
    result = self._query(query)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\cursors.py", line 321, in _query
    conn.query(q)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 860, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 1061, in _read_query_result
    result.read()
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 1349, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 1018, in _read_packet
    packet.check_error()
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 384, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\err.py", line 107, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1146, "Table 'stockset.data_fixed' doesn't exist")
>>> sql = """insert into basic_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
>>> sql = """insert into basic_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

SyntaxError: multiple statements found while compiling a single statement
>>> sql = """insert into basic_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
>>> curs.execute(sql,("123457", "LGDISPLAY", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000"))
1
>>> curs.execute(sql,("123458", "Hyundai", "500", "700", "800", "5000", "8000", "2000", "5000", "2800", "2200"))
1
>>> curs.execute(sql,("123457", "나라완", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000"))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    curs.execute(sql,("123457", "나라완", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000"))
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\cursors.py", line 165, in execute
    result = self._query(query)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\cursors.py", line 321, in _query
    conn.query(q)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 860, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 1061, in _read_query_result
    result.read()
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 1349, in read
    first_packet = self.connection._read_packet()
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 1018, in _read_packet
    packet.check_error()
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\connections.py", line 384, in check_error
    err.raise_mysql_exception(self._data)
  File "C:\Users\Celzook\AppData\Local\Programs\Python\Python36\lib\site-packages\pymysql\err.py", line 107, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.IntegrityError: (1062, "Duplicate entry '123457' for key 'PRIMARY'")
>>> curs.execute(sql,("123459", "나라완", "5500", "5700", "5800", "55000", "58000", "62000", "500000", "280000", "220000"))
1
>>> conn.commit()
>>> cur.execute(fetchall())
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cur.execute(fetchall())
NameError: name 'cur' is not defined
>>> curs.execute(fetchall())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    curs.execute(fetchall())
NameError: name 'fetchall' is not defined
>>> curs.execute(fetch())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    curs.execute(fetch())
NameError: name 'fetch' is not defined
>>> 
>>> curs.execute(fetchone())
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    curs.execute(fetchone())
NameError: name 'fetchone' is not defined
>>> curs.execute('select * from basic_fixed;')
4
>>> print(curs.fetchall())
(('123456', 'Samsung', '3310', '3350', '3650', '45000', '48000', '52000', '375000', '250000', '125000'), ('123457', 'LGDISPLAY', '5500', '5700', '5800', '55000', '58000', '62000', '500000', '280000', '220000'), ('123458', 'Hyundai', '500', '700', '800', '5000', '8000', '2000', '5000', '2800', '2200'), ('123459', '나라완', '5500', '5700', '5800', '55000', '58000', '62000', '500000', '280000', '220000'))
>>> curs.execute('select CODE from basic_fixed;')
4
>>> with conn.cursor() as curs:
	sql = "select CODE, DPT from basic_fixed;"
	curs.execute(sql)
	rs = curs.fetchall()
	for row in rs:
		print(row)

4
('123456', '125000')
('123457', '220000')
('123458', '2200')
('123459', '220000')
>>> with conn.cursor() as curs:
	sql = "select CODE, DPT from basic_fixed where NIQ2 < 5000;"
	curs.execute(sql)
	rs = curs.fetchall()
	for row in rs:
		print(row)

		
2
('123456', '125000')
('123458', '2200')
>>> with conn.cursor() as curs:
	sql = "select CODE, DPT from basic_fixed where NIQ2 < 5000;"
	curs.execute(sql)
	rs = curs.fetchall()
	for row in rs:
		print(row)
