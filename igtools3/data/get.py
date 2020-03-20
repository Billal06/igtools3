import pymysql

p = pymysql.connect("localhost", "root", "", "tools")
c = p.cursor()
c.execute("SELECT * FROM useragent")
data = []
for a in c:
	data.append(a[1])

print (data)
