__author__="bunkdeath"
__date__ ="$Dec 21, 2012 1:56:50 PM$"


class LiveSearch:
    
    def __init__(self, id, name,query):
        """
        """
        if not id.startswith("life_"):
            self.id = "life_%s"%id
        else:
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
         
        search_job = searcher.get_response(self.id)
        if type(search_job) is dict:
            return search_job
        else:
            self.response = search_job.get_response()

            return self.response
        
