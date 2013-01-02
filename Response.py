'''
Created on Dec 24, 2012

@author: mama
'''
class Response:
    
    def __init__(self, response_string):
        """
        """
        # extracted from chart
        self._status = ''
        self._original_search_id = ''
        self._total_count = ''
        self._raw_row = ''
        self._extra_fields = []
        self._time_range = []
        self._elapsed_time = ''
        self._version = ''
        self._grouping = []
        self._final = False
        self._columns = []
        self._aliases = []

        
        self.response_string = response_string
        self.data = {}
        type = self.response_string.get('type');
        if (type == "search"):
            self._parse_search_type()

        if(type == "chart"):
            self._parse_chart_type()
            
        if(type == "time"):
            self._parse_timechart_type()



    def _parse_search_type(self):
        pass

    def _parse_chart_type(self):
        print 'chat type'
        response_string = self.response_string
        self._status = response_string.get('status')
        self._original_search_id = response_string.get('orig_search_id')
        self._total_count = response_string.get('num_aggregated')
        self._raw_row = response_string.get('rows')
        self._extra_fields = response_string.get('extra_fields')
        self._time_range = response_string.get('time_range')
        self._elapsed_time = response_string.get('elapsed_seconds')
        self._version = response_string.get('version')
        self._grouping = response_string.get('grouping')
        self._final = response_string.get('final')
        self._columns = response_string.get('columns')
        self._aliases = response_string.get('aliases')

        print '----------------------------------------------'
        print '\n\n\n\n'
        print self._status
        print self._original_search_id
        print self._total_count
        print self._raw_row
        print self._extra_fields
        print self._time_range
        print self._elapsed_time
        print self._version
        print self._grouping
        print self._final
        print self._columns
        print self._aliases
        pass

    def get_rows(self):
        '''
        when this method is called, it returns the
        Rows object that hold
            """
            get rows iteratively
            get complete data at once
            """
        '''
        pass

    def get_raw_rows(self):
        '''
        this method upon called, returns raw row data that was
        returned in response as it is
        '''
        return self._raw_row

    def iterate(self):
        pass