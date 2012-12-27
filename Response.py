'''
Created on Dec 24, 2012

@author: mama
'''
class Response:
    
    def __init__(self, response):
        """
        """
        self.response = {}

        if (response["type"] == "search"):
            self.response_type_search(response)
            
        if(response["type"] == "time"):
            self.response_type_time(response)
            
        if(response["type"] == "chart"):
            self.response_type_chart(response)
            
    def response_livesearch(self,response):
        self.id = response["life_id"]
        self.query = response["query"]
        self.searchname = response["searchname"]
    
    def response_type_search(self,response):
        self.final = response["final"]
        self.estim_count = response["estim_count"]
        self.type = response["type"]
        self.data = "DataINSERT"
        
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
        
    
    def get_response(self):
        """
        """
        return self.response