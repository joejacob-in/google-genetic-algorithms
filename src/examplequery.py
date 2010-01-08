#!/usr/bin/env python
"""
example of how to use urllib2 and simplejson to query google
"""

import simplejson
import urllib
import urllib2

baseurl = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'


parameters = {'q': 'alternative splicing', 'start': 4}
#query = urllib.urlencode({'q': 'alternative splicing'})
queryurl = baseurl % urllib.urlencode(parameters)
print queryurl

opener = urllib2.build_opener()
f = opener.open(queryurl)

response = simplejson.load(f)
#print response

for result in response['responseData']['results']:
    print result['title']


if __name__ == '__main__':
    pass

