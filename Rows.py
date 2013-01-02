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

    def has_next(self):
        if self._index < self._count:
            return True
        else:
            return False
        pass

    def next(self):
        if self._index < self._count:
            ret = self._rows[self._index]
            self._index += 1
            return ret
        else:
            return 'Sorry, no more data'

    def get_rows(self):
        pass

    def reset(self):
        self._index = 0



    def _parse(self):
        aliases = self._response._aliases
        group_index = self._find_grouping_index('group', aliases)
        grouping = self._response._grouping
        
        for row in self._response._raw_row:
            self._count += 1
            row_data = {}
            i = 0
            for item in row:
                row_data[aliases[i]] = item
                i += 1

            self._rows.append(row_data)

    def _find_grouping_index(self, key, list):
        index = 0
        for item in list:
            if item == key:
                return index
            index += 1

        return -1