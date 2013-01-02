# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Jan 2, 2013 1:52:58 PM$"

class Rows:
    def __init__(self, response):
        self._response = response
        self._index = 0
        self._count = 0

        self._rows = []
        
        self._parse()
        pass

    def has_next(self):
        if self._index == self._count:
            pass
        pass

    def next(self):
        pass

    def get_rows(self):
        pass



    def _parse(self):
        aliases = self._response.get('aliases')
        for row in self._response.get('rows'):
            self._count += 1
            row = {}
            i = 0
            for item in row:
                row[aliases[i]] = item
                i += 1

            self._rows.append(row)