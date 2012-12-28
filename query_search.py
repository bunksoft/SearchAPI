# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:01 PM$"

search_job = searcher.search('error')
if search_job.has_error():
    print 'Query has error'
    print 'Error Message : ',  search_job.get_error()
else:
    response = search_job.get_response()
    print response
print '-----------------------'
search_job = searcher.search('error')
if search_job.has_error():
    print 'Query has error'
    print 'Error Message : ',  search_job.get_error()
else:
    response = search_job.get_response()
    print response
print '-----------------------'



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
