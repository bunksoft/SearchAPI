# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:31 PM$"


from LogPointSearcher import LogPointSearcher

searcher = LogPointSearcher()


logpoints = searcher.get_log_points()
for logpoint in logpoints:
    print logpoint.get_ip()
    print logpoint
    print '------------------'
print '------------------'

print 'ip : ', logpoints[1].get_ip()
print 'ip : ', logpoints[0].get_ip()