#!/usr/bin/env python
"""
Given a google query with the -q option, it launches it to google and returns the results.
"""
import simplejson
import urllib
import urllib2



def launch_query(query, start):
    """
    Execute a query on google, getting exactly 4 results.
    
    It appears that you can't get more than 4 results at a time with the google ajax APIs.
    To get more results for a query, you must launch this function multiple times changing the 'start' parameters.
    """
    baseurl = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'
    parameters = {'q': query, 'start': start}
    queryurl = baseurl % urllib.urlencode(parameters)
#    print queryurl

    opener = urllib2.build_opener()
    f = opener.open(queryurl)

    response = simplejson.load(f)
    for result in response['responseData']['results']:
        print result['title']




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('--query', metavar='query', type=str, nargs='+')

    args = parser.parse_args()
    query = args.query
    print query
    launch_query(query, 0)
    launch_query(query, 4)

