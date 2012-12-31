'''
Created on Dec 24, 2012

@author: mama
'''
class Response:
    
    def __init__(self, response_string):
        """
        """
        self.data = {}
        print "response_string-Response.py-line12 =>",response_string
        if (response_string["type"] == "search"):
            self.search(response_string)
            
        if(response_string["type"] == "time"):
            self.response_type_time(response_string)
            
        if(response_string["type"] == "chart"):
            self.response_type_chart(response_string)
    
    def search(self, response_string):
        self.final = response_string["final"]
        self.data = response_string['rows']
        self.total_count = response_string["estim_count"]
        self.type = response_string["type"]
        
    def response_type_time(self,response):
        self.final = response["final"]
        self.estim_count = response["estim_count"]
        self.type = response["type"]
        self.data = "DataINSERT"
        

        
    def response_type_chart(self,response):
        self.final = response["final"]
        self.estim_count = response["estim_count"]
        self.type = response["type"]
        self.data = "DataINSERT"

    def _extract_search_data(self, response_string):
        pass
        
    
    def get_response(self):
        """
        """
        return self.response