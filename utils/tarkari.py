'''
Created on Apr 11, 2015

@author: greenpaper
'''
import requests
import BeautifulSoup
from PyQt4.Qt import QThread,pyqtSignal


myurl = "http://kalimatimarket.com.np/home/rpricelist"
class DataDownloader(object):
    
    def getdata(self):
        req = requests.get(myurl).content
        return req


class ParserTarkari(DataDownloader):
    def get_tree(self):
        tree = BeautifulSoup.BeautifulSoup(self.getdata())
        first_data = tree.find("div", {"id":"datacontainer"}).findChild('table').findAll('tr')[0].findAll('td')
        return first_data
        
    def prepare_data(self):
        data = self.get_tree()
        new_data = []
        for i in range(len(data)):
            new_data.append(data[i].text)
        return new_data
    def show_it(self):
        print(self.get_tree())


class ParsetThread(ParserTarkari,QThread):
    dataready = pyqtSignal(list)
    def __init__(self):
        QThread.__init__(self)
    
    def run(self):
        data = self.prepare_data()
        
        self.dataready.emit(data)
        
    