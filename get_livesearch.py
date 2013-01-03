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
            for livesearch in livesearches:
#                livesearch.get_response()
                response_object = livesearch.get_response()
                print "\n Printing the response for live search."
                print response_object
#                response_object.get_response()
        else:
            print "Nothing found for your search"