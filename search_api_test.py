from Error import Error
from LogPointSearcher import LogPointSearcher

searcher = LogPointSearcher()

def display_rows(response):
    rows = response.get_rows()
    print

    for row in rows:
        print row

def display_iterative(response):
    print
    i = response.iterate()
    while i.has_next():
        dic =  i.next()
        for key in dic.keys():
            print key, ': ', dic[key]
        print '\n\n'

#print "############ GETTING QUERY RESULT ##############"    
##type = 'simple'
#query = ''
#
#search_job = searcher.search(query)
#
#if isinstance(search_job, Error):
#    print 'Error : ', search_job.get_error_message()
#    exit()
#
#if search_job.has_error():
#    print 'Error Message : ',  search_job.get_error()
#else:
#    response = search_job.get_response()
#    if isinstance(response, Error):
#        print 'Error : ', response.get_error_message()
#        exit()
#
#    display_rows(response)
#    display_iterative(response)
#
#    while not response.is_final():
#        response = search_job.get_response()
#        if isinstance(response, Error):
#            print 'Error : ', response.get_error_message()
#            exit()
#
#        display_rows(response)
#        display_iterative(response)
#
#print '#############################################'
#


#print "### GETTING LOGPOINTS INFORMATION #####"
#logpoints = searcher.get_log_points()
#if isinstance(logpoints, Error):
#    print 'Error : ', logpoints.get_error_message()
#else:
#    for logpoint in logpoints:
#        print "LogPoint name =", logpoint.name #print logpoint.get_name()
#        print "LogPoint ip =", logpoint.ip #print logpoint.get_ip()
#print "#####################################"


#print "###### GETING REPOS INFORMATION ##############"
#print "---- GETTING REPOS FROM ALL LOGPOINTS ---------"
#repos = searcher.get_repos()
#if isinstance(repos, Error):
#    print 'Error : ', repos.get_error_message()
#else:
#    for repo in repos:
#        print repo
#print "-----------------------"
#print "----- GETTING REPOS FROM LOGPOINTS -------"
#logpoints = searcher.get_log_points()
#if logpoints:
#    for logpoint in logpoints:
#        print "Repos for logpoint = ", logpoint.ip
#        repos = logpoint.get_repos()
#        if isinstance(repos, Error):
#            print 'Error : ', repos.get_error_message()
#        else:
#            print "-------- Repos for this LogPoint -----------"
#            for repo in repos:
#                print repo
#print "################################"


#print "###### GETING DEVICES INFORMATION ##############"
#print "---- GETTING DEVICES FROM ALL LOGPOINTS ---------"
#devices = searcher.get_devices()
#if isinstance(devices, Error):
#    print 'Error : ', devices.get_error_message()
#else:
#    for device in devices:
#        print device
#print "-----------------------"
#print "----- GETTING DEVICES FROM LOGPOINTS -------"
#logpoints = searcher.get_log_points()
#if not isinstance(logpoints,Error):
#    for logpoint in logpoints:
#        print "Devices for logpoint = ", logpoint.ip
#        devices = searcher.get_devices([logpoint])
#        if isinstance(devices, Error):
#            print 'Error : ', devices.get_error_message()
#        else:
#            print "-------- Devices for this LogPoint -----------"
#            for dev in devices:
#                print dev
#print "################################"



#print "#####    GETTING USER TIMEZONE   ####"
#time_zone = searcher.get_timezone()
#if isinstance(time_zone,Error):
#    print time_zone.get_error_message()
#else:
#    print time_zone
#print "#################################"


print "######### Getting LiveSearch  #########"
livesearches  = searcher.get_live_searches()
if isinstance(livesearches,Error):
    print livesearches.get_error_message()
else:
    for livesearch in livesearches:
        print livesearch.get_id()
        print livesearch.get_name()
        print livesearch.get_query()
        if isinstance(livesearch,Error):
            print 'Error message: ',livesearch.get_error_message()    
        else:
            response = livesearch.get_response()
            display_rows(response)
            display_iterative(response)
print "#####################"