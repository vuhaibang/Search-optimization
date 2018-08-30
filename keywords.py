from bs4 import BeautifulSoup
import requests
import time


start = time.time()
keywords = input('keywords:')
result = set()


#Google
page_google = 0
while True:
	page_google += 1
	url = 'https://www.google.com.vn/search?q={}&ei=StN7W6uFKdnj-AablrvoBQ&start={}'.format(keywords, page_google * 10)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	contents = soup.find_all('div', class_='s')
	if contents == []:
		break
	try:
		for content in contents:
			result.add(content.cite.text)
	except Exception as e:
		pass


#yahoo
page_yahoo = 0
while page_yahoo < 1:
	page_yahoo += 1
	url = 'https://vn.search.yahoo.com/search?p={}&b={}'.format(keywords, page_yahoo * 10)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	contents = soup.find_all('span', class_=" fz-ms fw-m fc-12th wr-bw lh-17")
	for content in contents:
		result.add(content.text)


#Bing
page_bing = 0
while page_bing < 30:
	page_bing += 1
	url = 'https://www.bing.com/search?q={}&first={}'.format(keywords, page_bing * 10)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	contents = soup.find_all('cite')
	for content in contents:
		result.add(content.text)


#baidu
page_baidu = 0
while page_baidu < 50:
	page_baidu += 1
	url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd={}&pn={}'.format(keywords, page_baidu * 10 - 1)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')
	contents = soup.find_all('div', class_='f13')
	try:
		for content in contents:
			index = content.a.text.rfind('/')
			result.add(content.a.text[: index])
	except:
		pass


total_time = time.time() -start
print('Total:{} website with keywords {} in {} s'.format(len(result), keywords, total_time))
for r in result:
	print(r)