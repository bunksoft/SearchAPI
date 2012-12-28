# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Dec 28, 2012 1:40:50 PM$"

from LogPointSearcher import LogPointSearcher

searcher = LogPointSearcher()

repos = searcher.get_repos()
if type(repos) is dict:
    if not repos.get('success'):
        print 'Something went wrong'
        print '\t', repos.get('message')
else:
    for repo in repos:
        print repo
print '-----------------------'