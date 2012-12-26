'''
Created on Dec 21, 2012

@author: mama
'''

class Repo:
    
    def __init__(self, logpoint, repo_name):
        """
        """
        self.logpoint = logpoint
        self.name = "%s/%s" % (logpoint, repo_name)
    
    def __str__(self):
        """
        """
        return self.name