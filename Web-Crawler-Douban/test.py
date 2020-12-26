# import urllib.request
# import urllib.parse

# form = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post", data=form)
# print(response.read().decode("utf-8"))

# try:
# 	response = urllib.request.urlopen("https://httpbin.org/get", timeout=1)
# 	print(response.read().decode("utf-8"))
# except urllib.error.URLError:
# 	print("Timed out!")

# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.getheader("Server"))

# url = "https://www.douban.com"
# headers = {
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# req = urllib.request.Request(url=url, headers=headers, method="POST")
# res = urllib.request.urlopen(req)
# print(res.read().decode("utf-8"))

# from bs4 import BeautifulSoup
# file = open("./index.html", 'rb')
# html = file.read()
# bs = BeautifulSoup(html, "html.parser")

# print(type(bs.meta.attrs))

# import xlwt

# book = xlwt.Workbook(encoding='utf-8')
# sheet = book.add_sheet('Sheet1')
# for i in range(9):
# 	for j in range(9):
# 		sheet.write(i, j, (i+1)*(j+1))
# book.save('qwq.xls')

import sqlite3
db = sqlite3.connect("demo.db")
print("Successfully opened database")
cur = db.cursor()
sql = "select id, name, address, salary from company"
cursor = cur.execute(sql)
for row in cursor:
    print("id = ", row[0], "name = ", row[1])
