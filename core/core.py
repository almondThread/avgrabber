# -*- coding: utf-8 -*-
from time import sleep
from random import uniform
from lxml import html
import requests
from utils.data import prepare_datetime, normalize_string
from utils.io import print_csv

BASE_URL = "https://www.avito.ru"
USERAGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
SESSION = requests.session()
SLEEP_MIN = 1
SLEEP_MAX = 5

def get(url):
    return SESSION.get(
        url,
        headers={'User-Agent': USERAGENT}
    )

def build_url(path):
    return BASE_URL + path


def list_view_pages(str):
    page_num = 1
    while True:
        url = build_url("/smolensk/bytovaya_elektronika?bt=1&p=%s&q=%s" % (page_num, str))
        page = get(url)
        view = html.fromstring(page.text)
        if view.xpath("//div[@class='nulus']"):
            break
        else:
            page_num += 1
            yield view

#def form_view(link):
#    page = get(build_url(link))
#    return html.fromstring(page.text)


def grab_list_element(element):
    descr_element = element.xpath("div[@class='description']")[0]

    link_element = descr_element.xpath("h3/a")[0]
    datetime = descr_element.xpath("div[@class='data']/div[@class='date']/text()")[0]
    price = descr_element.xpath("div[@class='about']/text()")[0]

    data_line = {
        'id':   link_element.get('href').split('_')[-1],
        'link': BASE_URL + link_element.get('href'),
        'title': link_element.text,
        'date': prepare_datetime(datetime),
        'price': normalize_string(price).split(" ")[0].replace("\u00A0", "")
    }
    return data_line
#
#def grab_form(form):
#    date = form.xpath("//div[@class='item-subtitle']/text()")
#
#    data_line = {
#        'date': date and date[0] or "",
#        'text': "".join(form.xpath("//div[@id='desc_text']/p/text()"))
#    }
#    return data_line

def search(str):

    for list in list_view_pages(str):
        ads = list.xpath("//div[@class='item item_table clearfix js-catalog-item-enum c-b-0']")
        for ad in ads:
            data_line = grab_list_element(ad)
            print_csv(data_line)
        sleep(uniform(SLEEP_MIN, SLEEP_MAX))


def multiple_search(strs):
    for str in strs:
        search(str)



