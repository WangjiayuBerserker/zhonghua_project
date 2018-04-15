import requests
from bs4 import BeautifulSoup

start_url = 'http://www.chinahr.com/haerbin/'

def get_channel_url(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    links = soup.select('div.sideBar > div:nth-of-type(2) > div:nth-of-type(5) >div.sideMain.hide > p:nth-of-type(2) > a')
    for link in links:
        page_url = link.get('href')
        print(page_url)

channel_list = '''
    http://www.chinahr.com/haerbin/jobs/23272/
    http://www.chinahr.com/haerbin/jobs/57227/
    http://www.chinahr.com/haerbin/jobs/31397/
    http://www.chinahr.com/haerbin/jobs/14897/
    http://www.chinahr.com/haerbin/jobs/46159/
    http://www.chinahr.com/haerbin/jobs/36792/
'''

# get_channel_url(start_url)