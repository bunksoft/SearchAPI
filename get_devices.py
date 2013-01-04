# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:41:07 PM$"

from LogPointSearcher import LogPointSearcher
from Error import Error

def get():
    searcher = LogPointSearcher()
    
    logpoints = searcher.get_log_points()
    if isinstance(logpoints, Error):
        print 'Error : ', logpoints.get_error_message()
    else:
        print '\n\n'
        print 'Searching for all allowed Devices'
        print '\n'
        devices = searcher.get_devices()
        if isinstance(devices, Error):
            print 'Error : ', devices.get_error_message()
        else:
            for device in devices:
                print device
        print '-----------------------'
        

        print '\n\n'
        print 'Searching Devices from ', logpoints[0]
        print '\n'
        
        devices = searcher.get_devices([logpoints[0]])
        if isinstance(devices, Error):
            print 'Error : ', devices.get_error_message()
        else:
            for device in devices:
                print device
        print '-----------------------'