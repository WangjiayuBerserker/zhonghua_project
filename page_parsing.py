import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
project_zh = client['project_zh']
url_list = project_zh['url_list']
item_info = project_zh['item_info']


# http://www.chinahr.com/haerbin/jobs/23272/2/
def get_links_from(url,page):
    start_url = '{}{}/'.format(url,str(page))
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text,'lxml')
    if  soup.find_all('li','l1'):
        links = soup.select('li.l1 > span.e1 > a')
        for link in links:
            item_list = link.get('href')
            data = {
                'url': item_list
            }
            url_list.insert_one(data)
    else:
        pass


def get_item_from(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    title = soup.select('span.job_name')[0].text if soup.find_all('span','job_name') else None
    price = soup.select('span.job_price')[0].text.split('-') if soup.find_all('span','job_price') else None
    area = soup.select('div.job_require > span.job_loc')[0].text.split() if soup.find_all('span','job_loc') else None
    line = soup.select('div.job_require > span:nth-of-type(4)') if soup.find_all('div','job_require') else None
    intro_info = soup.select('div.job_intro_info')[0].text.split()
    print(intro_info)


# get_links_from('http://www.chinahr.com/haerbin/jobs/23272/',1)
get_item_from('http://www.chinahr.com/job/5555957736505857.html')