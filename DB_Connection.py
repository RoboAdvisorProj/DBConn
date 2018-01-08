Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pymysql
>>> conn = pymysql.connect(host = 'localhost', user='root', password='1234', db='stockset', charset='utf8')
>>> curs = conn.cursor()
>>> sql = """insert into baisc_fixed(CODE, Name, NIQ2, NIQ1, NIQ0, SALEQ2, SALEQ1, SALEQ0, AST, CAP, DPT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
>>> 
