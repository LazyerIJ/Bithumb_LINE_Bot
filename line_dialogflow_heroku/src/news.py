from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import datetime

NEWS_LIST_FILE = './news_list.txt'
NEWS_URL = 'https://www.coinpress.co.kr'

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def sync_news_list(cur_time):
    create_time = modification_date(NEWS_LIST_FILE)
    if ((cur_time - create_time).seconds // 3600) > 1:
        return True
    return False


def news_time_to_datetime(time):
    time = time.text.split(' ')
    time = time[0][:-1] + ' ' + time[1] + ' ' + time[2][:-1]
    return datetime.datetime.strptime(time, '%Y %B %d')


def get_news(cur_dt, f_name=NEWS_LIST_FILE):
    rs = []
    rs_title = []
    rs_href = []

    #if (not os.path.exists(NEWS_LIST_FILE)) or sync_news_list(cur_dt):
    if True:
        f = open(NEWS_LIST_FILE, 'w')
        html = urlopen(NEWS_URL).read()
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.findAll("div",
                              'td-animation-stack')
        for t in titles:
            news_time = t.find('time')
            if not news_time:
                continue
            news_date = news_time_to_datetime(news_time)
            if cur_dt < news_date + datetime.timedelta(hours=48):
                bookmark = t.find('a', rel='bookmark')
                if bookmark:
                    href = bookmark.get_attribute_list('href')[0]
                    title = bookmark.get_attribute_list('title')[0]
                    f.write('{},{}'.format(title, href))

                    if title not in rs_title:
                        rs_title.append(title)
                        rs_href.append(href)
        f.close()
        for title, href in zip(rs_title, rs_href):
            rs.append({'title': title, 'href': href})
    else:
        f = open(NEWS_LIST_FILE, 'r')
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split(',')
            title = line[0]
            href = line[1]
            rs.append({'title': title, 'href': href})
    return rs


def titles_to_str(titles):
    rs = ''
    for item in titles:
        rs +='[{}]\n'.format(item['title'])
        rs += item['href'] + '\n'
    return rs


def add_ref_site(rs):
    return rs + '\nReference: {}'.format(NEWS_URL)



