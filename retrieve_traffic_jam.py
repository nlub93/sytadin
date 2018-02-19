'''
Script to download the traffic jam information from sytadin and store it inside a txt file
'''

import urllib2
from bs4 import BeautifulSoup
import datetime


class SytadinParser(object):
    
    def __init__(self):
        '''
        Initializes the parser
        '''
        self.url = 'http://www.sytadin.fr'
    
    def fetch_bouchon(self):
        '''
        Fetches the total number of kilometers of traffic jam
        '''
        request = urllib2.Request(self.url)
        f = urllib2.urlopen(request)
        soup = BeautifulSoup(f, 'html.parser')
        
        cumul_bouchon = soup.find(id='cumul_bouchon')
        for c in cumul_bouchon.children:
            if c.name == 'img':
                if c.attrs['alt'] != '':
                    bouchon = int(c.attrs['alt'].split(' ')[0])
                    break

        return bouchon

if __name__ == '__main__':
    parser = SytadinParser()
    current_min = datetime.datetime.now().minute
    while True:
        d = datetime.datetime.now()
        if d.minute != current_min:
            bouchon = parser.fetch_bouchon()
            print bouchon
            current_min = d.minute