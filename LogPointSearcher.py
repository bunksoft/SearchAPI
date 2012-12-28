import Config
__author__="bunkdeath"
__date__ ="$Dec 21, 2012 2:43:56 PM$"


import json
import time
import requests
from Config import Config
from LogPoint import LogPoint
from Device import Device
from SearchJob import SearchJob
from Repos import Repo
from Response import Response
from LiveSearch import LiveSearch


class LogPointSearcher:
    '''
    Searcher class to search for following
    '''
    def __init__(self):
        config = Config()
        self.ip = config.ip
        self.username = config.username
        self.secert_key = config.secret_key
        self.request_type = config.request_type


    def get_log_points(self):
        '''
        Returns list of LogPoint object
        '''
        """
            send requests to given IP using username and secret_key for type = "logpoints"
            our webserver should return [{"name": "", "ip":""}]
        """

        logpoints = []
        
        response = self._get_allowed_data('loginspects')
        allowed_logpoint = response['allowed_loginspects'];
        for data in allowed_logpoint:
            logpoints.append(LogPoint(data["ip"], data["name"]))

        return logpoints


    def get_repos(self, logpoints=None):
        ''' 
        Search for repos for which the user have permission to access
        according to credential provided

        If no parameter passed, it searches for the repos within
        all logpoints

        If logpoint object is passed as a parameter,
        it searches for the repos within the logpoint referenced
        by the logpoint object

        Returns list of Repo object
        '''

        if not logpoints:
            logpoints = []
            
        repos = []
        logpoint = {}
        logpoint_list = []
        
#        response = self._get_allowed_data('repos')
        for logpoint in logpoints:
            logpoint_list.append(logpoint.get_ip())

        response =  self._get_allowed_data("repos", logpoint_list)

        if not response.get('success'):
            return response
        
        allowed_repos = response.get('allowed_repos')
        logpoints = response.get('logpoint')
        '''
        get all the logpoints
        '''
        for logpt in logpoints:
            logpoint_ip = logpt.get('ip')
            logpoint_name = logpt.get('name')
            logpoint[logpoint_ip] = LogPoint(logpoint_ip, logpoint_name)

        '''
        get repo_name and its ip, and reference back to logpoint
        '''
        for repo in allowed_repos:
            address, repo_name = repo.get('address').split('/')
            repo_ip, port = address.split(':')
            repos.append(Repo(logpoint[repo_ip], repo_name))
        return repos

    def get_devices(self, logpoint=None):
        '''
        Search for devices for which the user have permission to access
        according to credential provided

        If no parameter passed, it searches for the devices within
        all logpoints

        If logpoint object is passed as a parameter,
        it searches for the devices within the logpoint referenced
        by the logpoint object

        Returns list of Device object
        '''
        
        devices = []
        logpoint = {}

        response = self._get_allowed_data('devices')
        if not response.get('success'):
            return response
        
        allowed_devices = response['allowed_devices'];
        logpoints = response['logpoint']

        '''
        get all the logpoints
        '''
        for logpt in logpoints:
            logpoint_ip = logpt.get('ip')
            logpoint_name = logpt.get('name')
            logpoint[logpoint_ip] = LogPoint(logpoint_ip, logpoint_name)
        

        for i in range(len(allowed_devices)):
            data = allowed_devices[i]
            if type(data) is dict:
                for row in data:
                    lp, ip = row.split('/')
#                    print ip, data[row], logpoint[lp]
                    devices.append(Device(ip, data[row], logpoint[lp]))
        
        return devices

    def get_live_searches(self):
        '''
        Returns list of LiveSearch object
        '''
        
        live_searches_lists = []
        
        live_searches =  self._get_allowed_data('livesearches')
        if live_searches.get("success"):
            for live_search in live_searches["livesearches"]:
                live_searches_lists.append(LiveSearch(live_search["life_id"],live_search["searchname"],live_search["query"]))#,"livesearch"))
        else:
            return live_searches_lists 
                
        return live_searches_lists

    def get_timezone(self):
        '''
        Returns timezone of user according to credential provided
        '''
        """
            webserver should return UTC or Asia/Kathmandu
        """

        return self._get_allowed_data('user_preference')['timezone']

    def search(self, query, timerange=None, repo=None, timeout=30, limit=100):
        '''
        Returns SearchJob object
        '''

        return self._get_search_job(query)

    def _get_allowed_data(self, data_type, logpoints=None):
        url = "%s://%s/%s" % (self.request_type, self.ip, "getalloweddata")

        data = {
                "username": self.username,
                "secret_key": self.secert_key,
                "type": data_type,
                "logpoints": json.dumps(logpoints)
                }

        print data

        try:
            ack = requests.post(url, data=data, timeout=10.0, verify=False)
        except Exception, e:
            resp = {}
            resp["success"] = False
            resp["message"] = str(e)
            print resp
            return resp

        ret = ''
        try:
            print ack.content
            ret = json.loads(ack.content)
        except:
            print ack.content

        return ret

    def _get_search_job(self, query):
        SEARCH_QUERY = query
        RESULT_LIMIT = 10
        SEARCH_TIME_RANGE = "Last 10 minutes"
        SEARCH_REPOS = []
        url = "%s://%s/%s" % (self.request_type, self.ip, "getsearchlogs")

        data = {
                "username":self.username,
                "secret_key": self.secert_key,
                "requestData": json.dumps({
                               "timeout": 30,
                               "client_name": "gui",
                               "repos": SEARCH_REPOS,
                               "starts": {},
                               "limit": RESULT_LIMIT,
                               "time_range": SEARCH_TIME_RANGE,
                               "query": SEARCH_QUERY
                            })
                }

        try:
            ack = requests.post(url, data=data, timeout=10.0, verify=False)
        except Exception, e:
            resp = {}
            resp["success"] = False
            resp["message"] = str(e)
            print resp
            return resp
        
        response = json.loads(ack.content)
        return SearchJob(response)
        

    def get_response(self, search_id):
        url = "%s://%s/%s" % (self.request_type, self.ip, "getsearchlogs")
        if search_id:
            data = {
                "username":self.username,
                "secret_key": self.secert_key,
                "requestData": json.dumps({
                           "search_id": search_id,
                           "waiter_id": "%s" % time.time(),
                           "seen_version": 0
                           })
                }

            start_time = time.time()
            response = {}
            i = 1
            while time.time() - start_time < 10.0:
                ack = requests.post(url, data=data, timeout=10.0, verify=False)
                res = json.loads(ack.content)
                if res.get('success'):
                    response = res
                if res['final'] == True:
                    break

            if not response:
                return {"success":False, "message":"No data from merger"}

            return response