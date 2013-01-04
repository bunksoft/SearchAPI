# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:41:23 PM$"

from LogPointSearcher import LogPointSearcher
from Error import Error
def get():
    searcher = LogPointSearcher()
    time_zone = searcher.get_timezone()
    print 'Getting Logpoint TimeZone'
    if isinstance(time_zone,Error):
        print time_zone.get_error_message()
    else:
        print time_zone
    print '-----------------------'