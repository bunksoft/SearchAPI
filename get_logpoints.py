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
        for logpoint in logpoints:
            print logpoint
    
        print
        print
        print
    
        for logpoint in logpoints:
            repos = logpoint.get_repos()
    
            if type(repos) is dict:
                if not repos.get('success'):
                    print 'Something went wrong'
                    print '\t', repos.get('message')
            else:
                for repo in repos:
                    print repo
            print '-----------------------'