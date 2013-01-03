__author__="bunkdeath"
__date__ ="$Dec 21, 2012 1:56:50 PM$"

from Response import Response

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
         
        response_string = searcher.get_response(self.id)
        
        return Response(response_string)
        
