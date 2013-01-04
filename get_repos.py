# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:50 PM$"

from LogPointSearcher import LogPointSearcher
from Error import Error

def get():
    searcher = LogPointSearcher()
    
    logpoints = searcher.get_log_points()
    if isinstance(logpoints, Error):
        print 'Error : ', logpoints.get_error_message()
    else:
#        for logpoint in logpoints:
#            print logpoint

        print '\n\n'
        print 'Getting all allowed Repos'
        print '\n'
        
        repos = searcher.get_repos()
        if isinstance(repos, Error):
            print 'Error : ', repos.get_error_message()
        else:
            for repo in repos:
                print repo
        print '-----------------------'

        print '\n\n'
        print 'Getting Repos from ', logpoints[1]
        print '\n'
        repos = searcher.get_repos([logpoints[1]])

        if isinstance(repos, Error):
            print 'Error : ', repos.get_error_message()
        else:
            for repo in repos:
                print repo
        print '-----------------------'