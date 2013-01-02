# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:50 PM$"

from LogPointSearcher import LogPointSearcher
def get():
    searcher = LogPointSearcher()
    
    logpoints = searcher.get_log_points()
    if type(logpoints) is dict:
        if not logpoints.get('success'):
            print 'Error : ', logpoints.get('message')
    else:
        for logpoint in logpoints:
            print logpoint

        print '\n\n'
        print 'Getting Repos from ', logpoints[1]
        print '\n'
        repos = searcher.get_repos([logpoints[1]])
    
        if type(repos) is dict:
            if not repos.get('success'):
                print 'Something went wrong'
                print '\t', repos.get('message')
        else:
            for repo in repos:
                print repo
        print '-----------------------'