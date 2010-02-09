#!/usr/bin/env python
"""
"""

import ConfigParser
import logging
import mechanize

bonzosurl = "http://www.bonzoscreek.com/forum"

def read_config():
    config = ConfigParser.RawConfigParser()
    config.read('config.txt')
    username = config.get('Bonzoscreek', 'username')
    password = config.get('Bonzoscreek', 'password')

    logging.debug((username, password))
    return username, password


def browse(username, password):
    br = mechanize.Browser()
    br.open(bonzosurl) 


if __name__ == '__main__':
    pass

