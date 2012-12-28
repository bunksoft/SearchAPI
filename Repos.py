'''
Created on Dec 21, 2012

@author: mama
'''

class Repo:
    
    def __init__(self, logpoint_name, repo_name):
        """
        """
        self._logpoint_name = logpoint_name
        self._repo_name = repo_name
        self._display_name = "%s/%s" % (logpoint_name, repo_name)

    def get_logpoint_name(self):
        '''
        returns respecitve logpoint name where the repo is held
        '''
        return self._logpoint_name

    def get_name(self):
        return self._repo_name
    
    def __str__(self):
        return self._display_name