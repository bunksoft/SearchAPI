# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:01 PM$"

from LogPointSearcher import LogPointSearcher
from LogPoint import LogPoint

def get():
####for chart query
#    def get(query = "| chart count() as Count, sum(sig_id) as SID by device_ip, source_name"):
####for timechart query
#    query = "| timechart count() as C, sum(sig_id) as SSID by device_ip, col_type"
####for log search
    query = '| chart count()'
    searcher = LogPointSearcher()

    lp = LogPoint('127.0.0.1', 'LogInspectHariTest')
    repos = lp.get_repos()
    repos_list = []
    for rep in repos:
        repos_list.append(rep.get_search_format())

        
    print '\n\n'
    print 'Getting SearchJob for given search query'
    print '\n'
    search_job = searcher.search(query, 'Last 30 days', repos_list)
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
            
            display(response)

            while not response.is_final():
                response = search_job.get_response()
                display(response)

    else:
        print search_job.get("message")


def display(response):
    rows = response.get_rows()
    print '\n\n'
    print 'Displaying data from list returned from get_rows()'
    print '\n\n'

    for row in rows:
        print row

    print '\n\n'
    print 'Iterative process for search response'
    print '\n\n'

    i = response.iterate()
    while i.has_next():
        dic =  i.next()
        for key in dic.keys():
            print key, ': ', dic[key]
        print '\n\n'