#!/usr/bin/env python
"""
main pipeline for the Genetic Algorithm
"""


import pyevolve
from pyevolve import GSimpleGA
from pyevolve.G2DList import G2DList
from launch_query import launch_query, print_fancy_results, get_key, GoogleQueryLimitsExceeded
import random
import re
import time
import datetime
import urllib2
# Fancy output
from TerminalColor import TerminalController    
import sys

debug = True

# define lower and upper limits for Ascii chars. Extreme values are 0, 255
rangemin = 0
rangemax = 255

# other parameters
#seq_length = 500
seq_length = 50
ngenerations = 10

global term
term = TerminalController()

notalpha_regex = re.compile('\W')

def start_logging():
    """
    write the results to a log file
    """
    now = datetime.datetime.now()
    logfilename = 'results/log_%s_%s_%s_%s:%s.txt' % (now.year, now.month, now.day, now.hour, now.minute)
    global logfile
    logfile = open(logfilename, 'wa')
    content = 'score\tgenotype\traw_genotype\n'
    logfile.write(content)
#    return logfile

def pickle_generation():
    print 'TODO: pickling '

#def count_results_fake(chromosome):
#    """
#    fake eval function for testing purposes
#    """
#    print term.render("${BOLD}CHROMOSOME:${NORMAL}"),
#    genotype = [chr(x) for x in chromosome.genomeList]
#    genotype = ''.join(genotype)
#    genotype = notalpha_regex.sub(' ', genotype)
#    print term.render(genotype),


class GoogleQueryGenome(pyevolve.G2DList.G2DList):
    """
    diploid genome, each chromosome is a string.
    """

def count_results_by_query(chromosome, debug=True):
    """
    """
    """
    Evaluate the score of a chromosome by:
    - transforming it to a string
    - calling a google query
    - counting results


    example input:
    >>> import random
    >>> chromosome = [chr(random.randrange(50,150)) for x in xrange(50)] # TODO: finish the doctest
    """
#    print "CHROMOSOME:", chromosome.genomeList, 
    genotypes = ([chr(x) for x in chromosome.genomeList[0]], [chr(x) for x in chromosome.genomeList[1]])
    genotypes = [''.join(genotype) for genotype in genotypes]
    genotypes = [notalpha_regex.sub(' ', genotype) for genotype in genotypes]
    print term.render("${BOLD}CHROMOSOME1:${NORMAL}"),
    print term.render(genotypes[0])
    print term.render("${BOLD}CHROMOSOME2:${NORMAL}"),
    print term.render(genotypes[1])
##    print results
##    print_fancy_results(results)
    if debug:
    # if the debug option is on, use a simpler way to calculate the score
        score = sum(1./len(re.findall('[\w]*', genotype)) for genotype in genotypes)
#        time.sleep(1)
    else:
        try:
            results = launch_query(genotype, google_api_key)
            time.sleep(1)
        except GoogleQueryLimitsExceeded:
            score = 0       # TODO: find a way to remove queries which return empty results
            print 'Google Query limit exceeded. No results'
            sys.exit(1) # TODO: it would be good to do something to pause the simulation here

        score = results['queries']['request'][0]['totalResults']

#        if not results['responseData']['cursor'].has_key('estimatedResultCount'):
#            score = 0
#        else:
#            score = int(results['responseData']['cursor']['estimatedResultCount'])
    print term.render("${RED}" + str(score) + "${NORMAL}")

    # to be written in the log file
    content = "%s\t%s\t%s\n" % (score, genotype, chromosome.genomeList)
    logfile.write(content)

#    print chromosome
#    print score
    return score


def run():
    """
    run the pipeline
    """
    global google_api_key
    google_api_key = get_key()

    start_logging()
    genome = GoogleQueryGenome(2, seq_length)
#    print genome
    genome.evaluator.set(count_results_by_query)
    genome.setParams(rangemin=rangemin, rangemax=rangemax)
    genome.initialize()
#    print genome
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(ngenerations)
#    ga.StepCallback.set(pickle_generation)
    ga.evolve(freq_stats=10)
    print "*"*5 + "best individual:"
    print ga.bestIndividual()



def test_evalWithRandomValues(seed):
    """
    if random.seed(0), this test should return something
    if random.seed(10), this test should return no results
    """
    random.seed(seed)
    chromosome = [chr(random.randrange(ascii_start, ascii_stop)) for x in xrange(seq_length)]
#    print chromosome
    res = count_results_by_query(chromosome)
    return res

def test_noresults():
    results = test_evalWithRandomValues(10)
    return results

def test_somesults():
    results = test_evalWithRandomValues(0)
    return results

def test_normalresults():
    chromosome = "alternative splicing"
    results = count_results_by_query([x for x in chromosome])
    return results

if __name__ == '__main__':
#    nores = test_noresults()
#    splicing = test_normalresults()

    run()
