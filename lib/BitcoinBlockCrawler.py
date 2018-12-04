import requests
import lxml.html as lh
import re
import math

class BitcoinBlockCrawler(object):

    def __init__(self,db,url):
        self.url = url
        self.db=db

    def start(self,url):

        #query the page
        page = requests.get(url)
        #parse HTML
        doc = lh.fromstring(page.content)
        #find the rows of the table and store
        tr_elements = doc.xpath('//tr')
        td_elements = doc.xpath('//tr//td')

        first_table_row = doc.xpath('.//table[@class="list"]/tr')
        for row in first_table_row:
            print('row ------')
            children = row.getchildren()
            # hash transaction
            a = children[0].xpath("*")
            # print senders

            #


