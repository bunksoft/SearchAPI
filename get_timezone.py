# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:41:23 PM$"

from LogPointSearcher import LogPointSearcher

def get():
    searcher = LogPointSearcher()

    print 'Getting Logpoint TimeZone'
    print searcher.get_timezone()
    print '-----------------------'