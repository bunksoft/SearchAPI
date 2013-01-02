# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:41:07 PM$"

from LogPointSearcher import LogPointSearcher
def get():
    searcher = LogPointSearcher()
    
    logpoints = searcher.get_log_points()
    if type(logpoints) is dict:
        if not logpoints.get('success'):
            print 'Error : ', logpoints.get('message')
    else:
        print '\n\n'
        print 'Searching for all allowed Devices'
        print '\n'
        devices = searcher.get_devices()
        if type(devices) is dict:
            if not devices.get('success'):
                print 'Something went wrong'
                print '\t', devices.get('message')
        else:
            for device in devices:
                print device
        print '-----------------------'
        

        print '\n\n'
        print 'Searching Devices from ', logpoints[0]
        print '\n'
        
        devices = searcher.get_devices([logpoints[0]])
        if type(devices) is dict:
            if not devices.get('success'):
                print 'Something went wrong'
                print '\t', devices.get('message')
        else:
            for device in devices:
                print device
        print '-----------------------'