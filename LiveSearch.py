__author__="bunkdeath"
__date__ ="$Dec 21, 2012 1:56:50 PM$"


class LiveSearch:
    
    def __init__(self, id, name,query):
        """
        """
        self.id = id
        self.name = name
        self.query = query

    def get_response(self):
        '''
        get_response() => returns response object

        This method returns the response object for the live search
        '''
        from LogPointSearcher import LogPointSearcher
        searcher = LogPointSearcher()
         
        search_job = searcher.search(self.query)
        self.response = search_job.get_response
#        if type(search_job) is not dict:
#            if search_job.has_error():
#                print 'Query has error'
#                print 'Error Message : ', search_job.get_error()
#            else:
##                This is the response object. livesearch response will be more the response.get_response.
#                response = search_job.get_response()
#                self.response = response
##                self.response = response.get_response(self)
#                
##            print '-----------------------'
#        else:
#            self.response = search_job.get("message")
##            print search_job.get("message")
        
        return self.response
