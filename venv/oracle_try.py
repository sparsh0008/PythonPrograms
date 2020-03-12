import cx_Oracle

con = cx_Oracle.connect("SYSTEM/Oracle123@localhost:1521/orcl")
cur = con.cursor()

sql = "select * from SPARSH2"

cur.execute(sql)
res = cur.fetchall()
print(res)