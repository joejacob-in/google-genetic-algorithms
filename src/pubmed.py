#!/usr/bin/env python
"""
Query the Pubmed database for articles matching a query, 
 and list them on the terminal.

Uses BioPython for querying and argparse to read arguments.
"""

"""Note to me: pmfetch accepts the following parameters:
<li>report=[docsum, brief, abstract, citation, medline, asn.1, mlasn1, uilist, sgml, gen] (Optional; default is asn.1)</li>
<li>mode=[html, file, text, asn.1, xml] (Optional; default is html)</li>
<li>dispstart - first element to display, from 0 to count - 1, (Optional; default is 0)</li>
<li>dispmax - number of items to display (Optional; default is all elements, from dispstart)</li>
<br/>See <a href="http://eutils.ncbi.nlm.nih.gov/entrez/query/static/efetch_help.html">help</a>.</body>
"""

youremail = 'giovanni.dallolio@upf.edu'

from Bio import Entrez
from TerminalColor import TerminalController
import logging
import re

Entrez.email = youremail

def pubmed(query):
    handle = Entrez.esearch(db="pubmed", term=query)
    record = Entrez.read(handle)

    id_list = record['IdList']
    logging.debug(id_list)

    search_results = Entrez.read(Entrez.epost("pubmed", id=",".join(id_list)))
    logging.debug(search_results)
    (webenv, querykey) = (search_results["WebEnv"], search_results["QueryKey"])

    fetch_handle = Entrez.efetch(db="pubmed", webenv=webenv, query_key=querykey, 
                        retmax=10, rettype="docsum", mode="text") 
    pretty_print(fetch_handle.readlines())

def pretty_print(reporttxt):
    """
    Pretty prints a report in the terminal, with colors
    """
    term = TerminalController()
    output = ''
    for line in reporttxt:
#        print line
        if re.match(' \w+', line):
            output += "${RED}%s${NORMAL}" % line
        else:
            output += line
    print term.render(output)
#    print output


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('-q', '--query', metavar='query', type=str, nargs='+', help='query', required=True)
    parser.add_argument('-d', '--debug', action='store_true', help='print debugging messages')
    parser.add_argument('-t', '--test', action='store_true', help='print debugging messages')

    args = parser.parse_args()
    if args.debug is True:
        logging.basicConfig(level=logging.DEBUG)
    query = args.query

    pubmed(query)

