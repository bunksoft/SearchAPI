# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:45:13 PM$"

from LogPointSearcher import LogPointSearcher
def get():
    '''get() => response object of live search.
     
    '''
    searcher = LogPointSearcher()
    
    livesearches  = searcher.get_live_searches()
    if type(livesearches) is dict:
    #    later needs to create a SearchJob object.
        if not livesearches.get("success"):
            print "Something went wrong."
    else:
        if len(livesearches) > 0:
            print "Livesearches Details:"
            for livesearch in livesearches:
                print "\n Livesearch id[life_id] =>",livesearch.id,"\n" \
                "\n Livesearch query => ",livesearch.query,"\n" \
                "\n Livesearch name => ",livesearch.name,"\n"
#                livesearch.get_response()
                response = livesearch.get_response()
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
            print "Nothing found for your search"