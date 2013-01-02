# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:01 PM$"

from LogPointSearcher import LogPointSearcher

def get(query = "| chart count() as Count, sum(sig_id) as SID by device_ip, source_name"):
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
            total_count = 0

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

    else:
        print search_job.get("message")