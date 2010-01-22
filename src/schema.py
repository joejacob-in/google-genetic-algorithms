#!/usr/bin/env python
"""
This module describes the SQLlite database which will store the results and the scores for every query.
It is meant to be used as a cache: if a query has already been ran recently, don't run it again.

"""


from elixir import *
from decorators import *


class Query(Entity):
    """
    for every query, store its score, and result
    """
    using_options(tablename = 'queries')
    
    query = Field(Text, primary_key=True)
    
    @slug_to_lower(query) 
    def __init__(self, query):
        """
        all queries are converted to lowercase
        """ 
        self.query = query.lower()
    




if __name__ == '__main__':
    pass

