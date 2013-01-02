# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:01 PM$"

from LogPointSearcher import LogPointSearcher

def get(query = "error"):
    searcher = LogPointSearcher()

    print '\n\n'
    print 'Getting SearchJob for given search query'
    print '\n'
    search_job = searcher.search(query)
    print '\n\n'
    if type(search_job) is not dict:
        if search_job.has_error():
            print 'Query has error'
            print 'Error Message : ',  search_job.get_error()
        else:
            print '\n\n'
            print 'Getting response from SearchJob'
            print '\n'
            response = search_job.get_response()
        print '-----------------------'
    else:
        print search_job.get("message")