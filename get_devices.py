# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:41:07 PM$"

from LogPointSearcher import LogPointSearcher

searcher = LogPointSearcher()


devices = searcher.get_devices()
if type(devices) is dict:
    if not devices.get('success'):
        print 'Something went wrong'
        print '\t', devices.get('message')
else:
    for device in devices:
        print device
print '-----------------------'