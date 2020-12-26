from bs4 import BeautifulSoup
import re
import urllib.request
import xlwt
import sqlite3

re_link = r'<a href="(.*?)"'
re_imgSrc = r'<img.*src="(.*?)"'
re_title = r'<span class="title">(.*)</span>'
re_rating = r'<span class="rating_num" property="v.average">(.*)</span>'
re_judge = r'<span>(\d*)人评价</span>'
re_inq = r'<span class="inq">(.*)</span>'
re_info = r'<p class="">(.*?)</p>'


def main():
	url = "https://movie.douban.com/top250?start="
	print("Crawling begins...")
	data = get(url)
	print("Success!")
	path = r'douban_movie_top250.xls'
	print("Saving at douban_movie_top250.xls...")
	save(data, path)
	print("Success!")
	path_db = r'movie.db'
	print("Saving at movie.db...")
	saveDB(data, path_db)
	print("Success!")


def get(base_url):
	data_list = []
	for i in range(10):
		url = base_url + str(i*25)
		html = getHTML(url)
		
		soup = BeautifulSoup(html, "html.parser")
		for item in soup.find_all("div", class_="item"):
			data = []
			item = str(item)

			link = re.findall(re_link, item)[0]
			data.append(link)
			imgSrc = re.findall(re_imgSrc, item, re.S)[0]
			data.append(imgSrc)
			title = re.findall(re_title, item)
			if len(title) == 2:
				zh = title[0]
				ot = title[1].replace('/', '')
				data.append(zh)
				data.append(ot)
			else:
				data.append(title[0])
				data.append('')
			rating = re.findall(re_rating, item)[0]
			data.append(rating)
			judge = re.findall(re_judge, item)[0]
			data.append(judge)
			inq = re.findall(re_inq, item)
			if len(inq) != 0:
				inq = inq[0].replace('。', '')
			else:
				inq = ''
			data.append(inq)
			info = re.findall(re_info, item, re.S)[0]
			info = re.sub(r'<br(\s*)?/>(\s*)?', '', info)
			info = re.sub('/', '', info)
			data.append(info.strip())

			data_list.append(data)

	return data_list


def save(data, path):
	book = xlwt.Workbook(encoding="utf-8", style_compression=0)
	sheet = book.add_sheet('Top 250 Douban Movies', cell_overwrite_ok=True)
	head = ('link', 'imgSrc', 'name-zh', 'name-ot', 'rate', 'no. rate', 'summ', 'info')
	
	for i in range(len(head)):
		sheet.write(0, i, head[i])
	for i in range(len(data)):
		for j in range(len(head)):
			sheet.write(i + 1, j, data[i][j])
	
	book.save(path)


def saveDB(data, path):
	initDB(path)
	db = sqlite3.connect(path)
	cur = db.cursor()
	for item in data:
		for i in range(len(item)):
			if i == 4 or i == 5:
				continue
			item[i] = '"' + item[i] + '"'
		sql = '''
		insert into movie250 (link, imgSrc, namezh, nameot, rate, norate, summ, info) 
		values (%s)
		''' % ', '.join(item)
		cur.execute(sql)
		db.commit()
	db.close()


def initDB(path):
	sql = '''
		create table movie250
		(
		id integer primary key autoincrement,
		link text,
		imgSrc text,
		namezh varchar,
		nameot varchar,
		rate numeric,
		norate numeric,
		summ text,
		info text
		)
	'''
	db = sqlite3.connect(path)
	cur = db.cursor()
	cur.execute(sql)
	db.commit()
	db.close()


def getHTML(url):
	head = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
	}
	req = urllib.request.Request(url=url, headers=head)
	html = ""

	try:
		res = urllib.request.urlopen(req)
		html = res.read().decode("utf-8")

	except urllib.error.URLError as e:
		if hasattr(e, "code"):
			print(e.code)
		if hasattr(e, "reason"):
			print(e.reason)
	return html


if __name__ == '__main__':
	main()
