#!/usr/bin/env python
"""
Given a google query with the -q option, it launches it to google and returns the results.
"""
import simplejson
import urllib
import logging
import urllib2

# Fancy output
from TerminalColor import TerminalController    

class GoogleQueryLimitsExceeded(Exception):
    """
    I have a limit of 100 queries per day. This exception is raise when the limit has been reached.
    """
    def __init__(self):
        pass
    def __repr__(self):
        return repr('Sorry, Google query limit exceeded')


def get_key():
    """
    parse config file and get the google api key
    """
    # read the google api key
    configfile = open('configfile.txt', 'r')
    key = configfile.read().strip()
    return key

def launch_query(query, key):
    """
    Execute a query on google, getting exactly 4 results.
    
    It appears that you can't get more than 4 results at a time with the google ajax APIs.
    To get more results for a query, you must launch this function multiple times changing the 'start' parameters.
    """
    baseurl = 'https://www.googleapis.com/customsearch/v1?%s'
#    parameters = {'q': query, 'start': start, 'key': key}
    # parameters needed: q, cx, key
    parameters = {'q': query, 'cx': '017576662512468239146:omuauf_lfve', 'key': key}
    queryurl = baseurl % urllib.urlencode(parameters)
    logging.debug(queryurl)

    opener = urllib2.build_opener()
    try:
        f = opener.open(queryurl)
    except urllib2.URLError:    
        raise GoogleQueryLimitsExceeded

    response = simplejson.load(f)
#    print response
#    for result in response['responseData']['results']:
#        print result['title']

    return response

def print_fancy_results(response):
    term = TerminalController()
    logging.debug(response)
    number_results = response['queries']['request'][0]['totalResults']
    print term.render('${RED}Showing the first 10 results out of %s:${NORMAL}' % number_results)
    if number_results == 0:
        print 'no results'
    else:
        for result in response['items']:
            output = '- ${BLUE}' + result['title'] + '${NORMAL} (' + result['link'] + ')'
            print term.render("%s" % output)
        


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('-q', '--query', metavar='query', type=str, nargs='+', help='query', required=True)
    parser.add_argument('-d', '--debug', action='store_true', help='print debugging messages')

    args = parser.parse_args()
    if args.debug is True:
        logging.basicConfig(level=logging.DEBUG)
    query = args.query
    print query

    key = get_key()
    results1 = launch_query(query, key)
    print_fancy_results(results1)
#    results2 = launch_query(query, 4)
#    print_fancy_results(results2)

