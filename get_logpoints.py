# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:31 PM$"


from LogPointSearcher import LogPointSearcher
def get():
    searcher = LogPointSearcher()
    
    logpoints = searcher.get_log_points()
    if type(logpoints) is dict:
        if not logpoints.get('success'):
            print 'Error : ', logpoints.get('message')
    else:
        print '\n\nGetting all allowed logpoints'
        print '-------------------------------'
        for logpoint in logpoints:
            print logpoint