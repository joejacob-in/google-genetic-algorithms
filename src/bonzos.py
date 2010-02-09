#!/usr/bin/env python
"""
"""

import ConfigParser
import logging
import mechanize
import pdb

bonzosurl = "http://www.bonzoscreek.com/forum"

def read_config():
    config = ConfigParser.RawConfigParser()
    config.read('config.txt')
    username = config.get('Bonzoscreek', 'username')
    password = config.get('Bonzoscreek', 'password')

    logging.debug((username, password))
    return username, password


def bonzo_connect(username, password):
    logging.debug("Bonzo's power!")
    br = mechanize.Browser()
    br.open(bonzosurl) 
    logging.debug(br.title())

    # select the login form and fill it
    br.select_form(nr=0)
    br['username'] = username
    br['password'] = password
    r1 = br.submit()
    pdb.set_trace()

    return br

if __name__ == '__main__':
    try:
        (username, password) = read_config()
    except ConfigParser.NoSectionError:
        print 'no config file present'
    br = bonzo_connect(username, password)

