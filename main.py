from Repos import Repo
from LogPoint import LogPoint
from LogPointSearcher import LogPointSearcher

#searcher = LogPointSearcher(ip="192.168.2.205", username="admin", secret_key="29cc708f5cee084bb9d7b8c704d6f8e3")
searcher = LogPointSearcher()

##OK test
#for logpoint in searcher.get_log_points():
#    print logpoint
#print '-----------------------'

##OK
repos = searcher.get_repos()
if type(repos) is dict:
    if not repos.get('success'):
        print 'Something went wrong'
        print '\t', repos.get('message')
else:
    for repo in repos:
        print repo
print '-----------------------'
#for repo in searcher.get_repos():
#    print repo
#print '-----------------------'
#
##OK
#devices = searcher.get_devices()
#if type(devices) is dict:
#    if not devices.get('success'):
#        print 'Something went wrong'
#        print '\t', devices.get('message')
#else:
#    for device in devices:
#        print device
#print '-----------------------'
#
##Ok
#for livesearch in searcher.get_live_searches():
#    print livesearch

##OK
#print searcher.get_timezone()
#print '-----------------------'
#
#
#search_job = searcher.search('error')
#if search_job.has_error():
#    print 'Query has error'
#    print 'Error Message : ',  search_job.get_error()
#else:
#    response = search_job.get_response()
#    print response
#print '-----------------------'




#query = "error"
#logpoint = LogPoint("10.45.1.1")
#repos = [Repo("_loginspect", logpoint), Repo("default", logpoint)]
#time_range = "Last 10 minutes"
#
#search_job = searcher.search(query=query, repos=repos, time_range=time_range, timeout=30, limit=100)
#
#print search_job.has_error()
#print search_job.get_error()
#print search_job.get_response()
#print search_job.get_type()
#print search_job.is_timeout()
#print search_job.get_time_range()
#search_job.cancel()
#    pass
#print search_job
