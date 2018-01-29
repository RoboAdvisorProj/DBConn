import pymysql
import math

# MySQL Connection
conn = pymysql.connect(host='52.79.187.44', port=3306, user='root', password='1234', db='ipo', charset='utf8')
cursor = conn.cursor(pymysql.cursors.SSCursor)

# <NI3Y>
# Get Numb From ad_indicator
sql = "select Numb from ad_indicator"
cursor.execute(sql)

# Save Numb at Numblist
Numblist = cursor.fetchall()
print(Numblist)

# Numb값들에 대한 반복문 수행
for Numb in Numblist:
    # Numb값과 일치하는 Row 가져옴
    sql = "select NIY0, NIY1, NIY2 from basic_fixed where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    # 가져온 데이터를 각 변수에 저장후 계산 수행
    NIY0 = float(current_row[0])
    NIY1 = float(current_row[1])
    NIY2 = float(current_row[2])
    NI3Y = (math.log(NIY1 / NIY2) + math.log(NIY0 / NIY1)) * 0.5

    print(NI3Y)

    # 계산이 완료된 데이터를 데이터베이스에 업데이트
    sql = "update ad_indicator set NI3Y = " + str(NI3Y) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)


# <SALE3Y>
sql = "select Numb from ad_indicator"
cursor.execute(sql)

Numblist = cursor.fetchall()

for Numb in Numblist:
    sql = "select SALEY0, SALEY1, SALEY2 from basic_fixed where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    SALEY0 = int(current_row[0])
    SALEY1 = int(current_row[1])
    SALEY2 = int(current_row[2])
    SALE3Y = (math.log(SALEY1 / SALEY2) + math.log(SALEY0 / SALEY1)) * 0.5

    print(round(SALE3Y, 4))

    sql = "update ad_indicator set SALE3Y = " + str(SALE3Y) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)

# <DEPRT>
sql = "select Numb from ad_indicator"
cursor.execute(sql)

Numblist = cursor.fetchall()

for Numb in Numblist:
    sql = "select AST, DPT from basic_fixed where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    AST = int(current_row[0])
    DPT = int(current_row[1])
    DEPRT = DPT / AST

    print(DEPRT)

    sql = "update ad_indicator set DEPRT = " + str(DEPRT) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)

# <VOL_D>
sql = "select Numb from ad_indicator"
cursor.execute(sql)

Numblist = cursor.fetchall()

for Numb in Numblist:
    sql = "select D_PRH, D_PRL from basic_variation where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    D_PRH = int(current_row[0])
    D_PRL = int(current_row[1])
    VOL_D = (D_PRH - D_PRL) / ((D_PRH + D_PRL) / 2)

    print(VOL_D)

    sql = "update ad_indicator set VOL_D = " + str(VOL_D) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)

# <VOL_Y>
sql = "select Numb from ad_indicator"
cursor.execute(sql)

Numblist = cursor.fetchall()
for Numb in Numblist:
    sql = "select Y_PRH, Y_PRL from basic_variation where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    Y_PRH = int(current_row[0])
    Y_PRL = int(current_row[1])
    VOL_Y = (Y_PRH - Y_PRL) / ((Y_PRH + Y_PRL) / 2)

    print(VOL_D)

    sql = "update ad_indicator set VOL_Y = " + str(VOL_Y) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)

# <ROA>

sql = "select Numb from ad_indicator"
cursor.execute(sql)

Numblist = cursor.fetchall()

for Numb in Numblist:
    sql = "select NIY0, AST from basic_fixed where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    NIY0 = int(current_row[0])
    AST = int(current_row[1])
    ROA = NIY0 / AST
    print(ROA)

    sql = "update ad_indicator set ROA = " + str(ROA) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)

# <ROE>

sql = "select Numb from ad_indicator"
cursor.execute(sql)

Numblist = cursor.fetchall()

for Numb in Numblist:
    sql = "select NIY0, CAP from basic_fixed where Numb='" + Numb[0] + "';"
    print(sql)
    cursor.execute(sql)
    current_row = cursor.fetchone()

    NIY0 = int(current_row[0])
    CAP = int(current_row[1])
    ROE = NIY0 / AST
    print(ROA)

    sql = "update ad_indicator set ROE = " + str(ROE) + " where Numb='" + Numb[0] + "';"
    cursor.execute(sql)

conn.commit()
cursor.close()
# 수행결과 데이터베이스에 커밋

'''
class stock_selection:


# <1. 위험중립 조건식>
def risk_neutral():
    curs = conn.cursor()
    sql = "select CODE, Name, Price, ROE, BETA, Chan from ad_indicator where Value >=  500 and PER <= 11.0 and ROE >= 8 and ROA >= 5 and BETA >= 1.2 and NIY0 > 0 and NI3Y > 0 and SALE3Y > 0 and DEPRT < 50 and PBR < 1.5 and D_IV = YES and VOL_Y <= 50 and VOL_D <= 10;"
    curs.execute(sql)
    rs = curs.fetchall()
    for row in rs:
        print(row)


# <2. 안정추구 조건식>
def safe_prefer():
    curs = conn.cursor()
    sql = "select CODE, Name, Price, ROE, BETA, Chan from ad_indicator where Value >=  1000 and PER <= 7.0 and ROE >= 10 and ROA >= 6 and BETA <= 1.2 and NIY0 > 0 and NI3Y > 0 and SALE3Y > 0 and DEPRT < 40 and PBR < 1.3 and D_IV = YES and VOL_Y <= 30 and VOL_D <= 7;"
    curs.execute(sql)
    rs = curs.fetchall()
    for row in rs:
        print(row)


# <3. 안정형 조건식>
def safe_main():
    curs = conn.cursor()
    sql = "select CODE, Name, Price, ROE, BETA, Chan from ad_indicator where Value >=  2500 and PER <= 3.0 and ROE >= 3 and ROA >= 5 and BETA <= 1.15 and NIY0 > 0 and NI3Y > 0 and SALE3Y > 0 and DEPRT < 30 and PBR < 1.0 and D_IV = YES and VOL_Y <= 20 and VOL_D <= 5;"
    curs.execute(sql)
    rs = curs.fetchall()
    for row in rs:
        print(row)


# <4. 적극투자 조건식>
def risk_prefer():
    curs = conn.cursor()
    sql = "select CODE, Name, Price, ROE, BETA, Chan from ad_indicator where Value >=  200 and ROE >= 6 and ROA >= 5 and BETA >= 1.5 and NIY0 > 0 and NI3Y > 0 and SALE3Y > 0 and DEPRT < 80 and PBR < 2.0 and VOL_Y <= 80 and VOL_D <= 15;"
    curs.execute(sql)
    rs = curs.fetchall()
    for row in rs:
        print(row)


# <5. 공격투자 조건식>
def risk_agg():
    curs = conn.cursor()
    sql = "select CODE, Name, Price, ROE, BETA, Chan from ad_indicator where ROE >= 12 and BETA >= 2.0;"
    curs.execute(sql)
    rs = curs.fetchall()
    for row in rs:
        print(row)
'''
