# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:45:13 PM$"
from Error import Error
from LogPointSearcher import LogPointSearcher
def get():
    '''get() => response object of live search.
     
    '''
    searcher = LogPointSearcher()
    livesearches  = searcher.get_live_searches()
    
    print "__________Live search Details_________:"
    if isinstance(livesearches,Error):
        print livesearches.get_error_message()
    else:
        for livesearch in livesearches:
            if not isinstance(livesearch,Error):
                print "\n Livesearch-id[life_id] =>",livesearch.get_id(),"\n" \
                "\n Livesearch-query => ",livesearch.get_query(),"\n" \
                "\n Livesearch-name => ",livesearch.get_name(),"\n"
    
                response = livesearch.get_response()
                if isinstance(response,Error):
                    print "\n\n\nError\t\t\t\t\n\n\n",response.get_error_message(),"\n\n\n\n"
                else:
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
                print livesearch.get_error_message()
