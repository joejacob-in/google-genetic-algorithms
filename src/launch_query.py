#!/usr/bin/env python
"""
Given a google query with the -q option, it launches it to google and returns the results.
"""






if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('--query', metavar='query', type=str, nargs='+')

    args = parser.parse_args()
    print args.query
    print dir(args)

