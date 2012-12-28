'''
Created on Dec 21, 2012

@author: mama
'''
class LogPoint:
    
    def __init__(self, ip, name=None):
        """
        logpoint ip address
        logpoint name
        """
        self.ip = ip
        if name:
            self.name = name
        else:
            self.name = self.ip.replace(".", "_")

    def get_ip(self):
        return self.ip

    def get_repos(self):
        searcher = LogPointSearcher()
        pass
    
    def __str__(self):
        """
        """
        return self.name