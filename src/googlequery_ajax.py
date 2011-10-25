#!/usr/bin/env python
"""
example of how to use urllib2 and simplejson to query google
"""

import simplejson
import urllib
import urllib2
import time
import argparse
import logging

baseurl = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'


#parameters = {'q': 'alternative splicing', 'start': 4}
#query = urllib.urlencode({'q': 'alternative splicing'})
def launch_query_ajax(query, start=0):
	"""
	Launch a query through the ajax APIs
	"""
	parameters = {'q': query, 'start':start}
	queryurl = baseurl % urllib.urlencode(parameters)
	print queryurl

	# TODO: implement a UserAgent and possibly use WebBrowser
	opener = urllib2.build_opener()
	f = opener.open(queryurl)

	response = simplejson.load(f)
	logging.debug(response)
	results_count = response['responseData']['cursor']['estimatedResultCount']
	print 'showing 4 results of', results_count

	for result in response['responseData']['results']:
	    print result['title']
	logging.debug(result)
	time.sleep(1)
	return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('-q', '--query', metavar='query', type=str, nargs='+', help='query', required=True)
    parser.add_argument('-d', '--debug', action='store_true', help='print debugging messages')

    args = parser.parse_args()
    if args.debug is True:
        logging.basicConfig(level=logging.DEBUG)
    query = args.query
    print query

    response = launch_query_ajax(query, start=0)
#    print_fancy_results(results1)


