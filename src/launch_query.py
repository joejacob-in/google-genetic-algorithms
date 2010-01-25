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


def launch_query(query, start):
    """
    Execute a query on google, getting exactly 4 results.
    
    It appears that you can't get more than 4 results at a time with the google ajax APIs.
    To get more results for a query, you must launch this function multiple times changing the 'start' parameters.
    """
    baseurl = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'
    parameters = {'q': query, 'start': start}
    queryurl = baseurl % urllib.urlencode(parameters)
    logging.debug(queryurl)

    opener = urllib2.build_opener()
    f = opener.open(queryurl)

    response = simplejson.load(f)
#    for result in response['responseData']['results']:
#        print result['title']

    return response

def print_fancy_results(response):
    term = TerminalController()
    for result in response['responseData']['results']:
        output = result['title'].replace("<b>", "${BOLD}").replace("</b>", "${NORMAL}")
        print term.render("%s (%s)" % (output,result['url']))
        


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
    print_fancy_results(launch_query(query, 0))
    print_fancy_results(launch_query(query, 4))

