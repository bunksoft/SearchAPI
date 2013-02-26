import json
import time
import Config
import requests
from Config import Config
from LogPoint import LogPoint
from Device import Device
from SearchJob import SearchJob
from Repos import Repo
from LiveSearch import LiveSearch
from Error import Error

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
        if isinstance(response, Error):
            return response
        else:
            if not response.get('success'):
                return Error(response.get('message'));
            
            allowed_logpoint = response['allowed_loginspects'];
            for data in allowed_logpoint:
                logpoints.append(LogPoint(data["ip"], data["name"]))

            return logpoints

    def get_repos(self, logpoint_object=None):
        ''' 
        Search for repos for which the user have permission.

        If no parameter passed, it searches for the allowed repos in all logpoints

	'''
        if not logpoint_object:
            logpoint_object = []
                
        repos = []
        logpoint = {}
        logpoint_list = []
        
        for logpoint_row in logpoint_object:
            lp = logpoint_row.get_ip()
            logpoint_list.append(lp)
	    
        response =  self._get_allowed_data("repos", logpoint_list)
        if isinstance(response, Error):
            return response

        if not response.get('success'):
            return Error(response.get('message'))
        
        allowed_repos = response.get('allowed_repos')
        response_logpoints = response.get('logpoint')

        if response_logpoints:
            for logpt in response_logpoints:
                logpoint_ip = logpt.get('ip')
                logpoint_name = logpt.get('name')
                logpoint[logpoint_ip] = LogPoint(logpoint_ip, logpoint_name)
        else:
            for logpt in logpoint_object:
                logpoint[logpt.get_ip()] = logpt

        for repo in allowed_repos:
            address, repo_name = repo.get('address').split('/')
            logpoint_ip, port = address.split(':')
	    if not logpoint_list:
		repos.append(Repo(logpoint[logpoint_ip], repo_name))
	    elif logpoint_ip in logpoint_list:
		repos.append(Repo(logpoint[logpoint_ip], repo_name))
        return repos

    def get_devices(self, logpoint_list=None):
        '''
        If no parameter passed, it searches for the allowed devices within
        all logpoints otherwise allowed devices are searched in the logpoint

        Returns list of Device object
        '''
        
        devices = []
        logpoint = {}

        response = self._get_allowed_data('devices')
        if isinstance(response, Error):
            return response
        
        if not response.get('success'):
            return Error(response.get('message'))
        
        allowed_devices = response['allowed_devices'];
        logpoints = response['logpoint']
        for logpt in logpoints:
            logpoint_ip = logpt.get('ip')
            logpoint_name = logpt.get('name')
            logpoint[logpoint_ip] = LogPoint(logpoint_ip, logpoint_name)

        for device_info in allowed_devices:
	    if type(device_info) is dict:
		for li_dev_ip, dev_name in device_info.iteritems():
		    lp, ip = li_dev_ip.split('/', 1)
		    if not logpoint_list:
			devices.append(Device(ip, device_info[li_dev_ip], logpoint[lp]))
		    else:
			for requested_logpoint in logpoint_list:
			    if lp == requested_logpoint.get_ip():
				devices.append(Device(ip, device_info[li_dev_ip], logpoint[lp]))
			
        return devices

    def get_live_searches(self):
        '''
        Returns list of LiveSearch object
        '''
        
        live_searches_lists = []
        try:
            live_searches =  self._get_allowed_data('livesearches')
	    if not isinstance(live_searches,Error):
		if live_searches.get("success"):
		    for live_search in live_searches["livesearches"]:
			live_searches_lists.append(LiveSearch(live_search["life_id"],live_search["searchname"],live_search["query"]))
		    return live_searches_lists
		else:
		    return Error(live_searches["message"])
	    else:
		return live_searches
	except Exception, e:
	    return Error(str(e))

    def get_timezone(self):
        '''
        Returns timezone of user according to credential provided
        '''
        """
            webserver should return UTC or Asia/Kathmandu
        """
        time_zone = self._get_allowed_data('user_preference')
        if isinstance(time_zone, Error):
            return time_zone
        else:
            if not time_zone.get("success"):
                return Error(time_zone.get("message"))
                
            else:
                return time_zone.get("timezone")

    def search(self, query, timerange=None, repo=None, timeout=30, limit=100):
        '''
        Returns SearchJob object
        '''

        return self._get_search_job(query, timerange, repo, timeout, limit)

    def _get_allowed_data(self, data_type, logpoints=None):
        url = "%s://%s/%s" % (self.request_type, self.ip, "getalloweddata")

        data = {
                "username": self.username,
                "secret_key": self.secert_key,
                "type": data_type,
                "logpoints": json.dumps(logpoints)
                }
        try:
            ack = requests.post(url, data=data, timeout=10.0, verify=False)
        except Exception, e:
            return Error(str(e))
        try:
            ret = json.loads(ack.content)
        except Exception, e:
            ret = Error(str(e))
        finally:
	    return ret
    
    def _get_search_job(self, query, timerange=None, repo=None, timeout=None, limit=None):
        SEARCH_QUERY = query
        
        if not timerange:
            SEARCH_TIME_RANGE = 'Last 10 minutes'
        else:
            SEARCH_TIME_RANGE = timerange
        if not repo:
            SEARCH_REPOS = []
        else:
            SEARCH_REPOS = repo

        if not timeout:
            timeout = 10

        if not limit:
            RESULT_LIMIT = 30
        else:
            RESULT_LIMIT = limit

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
            ack = requests.post(url, data=data, timeout=20.0, verify=False)#verify = True => SSL certificate will be verified.
        except Exception, e:
            return Error(str(e))
        
        response = json.loads(ack.content)
        return SearchJob(response)
        
    def get_response(self, search_id, version=None):
        if not version:
            version = 0
        url = "%s://%s/%s" % (self.request_type, self.ip, "getsearchlogs")
	if search_id:
            data = {
                "username":self.username,
                "secret_key": self.secert_key,
                "requestData": json.dumps({
                           "search_id": search_id,
                           "waiter_id": "%s" % time.time(),
                           "seen_version": version
                           })
                }
            start_time = time.time()
            while time.time() - start_time < 10.0:
                try:
                    ack = requests.post(url, data=data, timeout=10.0, verify=False)
		    res = json.loads(ack.content)
                    if res.get('success'):
			response = res
                    else:
                        response = Error(res.get("message"))
                    if res['final'] == True:
                        break
                except Exception, e:
                    response = Error('Error on query process. %s' % str(e))
	    return response