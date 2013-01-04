# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:31 PM$"

from Error import Error

from LogPointSearcher import LogPointSearcher
def get():
    searcher = LogPointSearcher()
    
    logpoints = searcher.get_log_points()
    if isinstance(logpoints, Error):
        print 'Error : ', logpoints.get_error_message()
    else:
        print '\n\nGetting all allowed logpoints'
        print '-------------------------------'
        for logpoint in logpoints:
            print logpoint