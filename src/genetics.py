#!/usr/bin/env python
"""
main pipeline for the Genetic Algorithm
"""


import pyevolve as pv
from pyevolve import GSimpleGA
from pyevolve import G1DList
from launch_query import launch_query, print_fancy_results, get_key
import random
import re
import time
import datetime
import urllib2

debug = False

# define lower and upper limits for Ascii chars. Extreme values are 0, 255
rangemin = 0
rangemax = 255

# other parameters
seq_length = 500
ngenerations = 10



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

def eval_func(chromosome):
    """
    Evaluate the score of a chromosome by:
    - transforming it to a string
    - calling a google query
    - counting results


    example input:
    >>> import random
    >>> chromosome = [chr(random.randrange(50,150)) for x in xrange(50)]
    """
#    print "CHROMOSOME:", chromosome.genomeList, 
    print "CHROMOSOME:",
    genotype = [chr(x) for x in chromosome.genomeList]
    genotype = ''.join(genotype)
    genotype = notalpha_regex.sub(' ', genotype)
    print genotype,
##    print results
##    print_fancy_results(results)
    if debug:
    # if the debug option is on, use a simpler way to calculate the score
        score = len(re.findall('[\w ]', genotype))
    else:
        try:
            results = launch_query(genotype, google_api_key)
            time.sleep(2)
        except urllib2.URLError:
            score = -100
            print 'no results'
            return score # TODO: ugly to have a return here

        score = results['queries']['request'][0]['totalResults']

#        if not results['responseData']['cursor'].has_key('estimatedResultCount'):
#            score = 0
#        else:
#            score = int(results['responseData']['cursor']['estimatedResultCount'])
    print score

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
    genome = G1DList.G1DList(seq_length)
    genome.evaluator.set(eval_func)
    genome.setParams(rangemin=rangemin, rangemax=rangemax)
    genome.initialize()
#    print genome
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(ngenerations)
    ga.evolve(freq_stats=10)
    print ga.bestIndividual()



def test_evalWithRandomValues(seed):
    """
    if random.seed(0), this test should return something
    if random.seed(10), this test should return no results
    """
    random.seed(seed)
    chromosome = [chr(random.randrange(ascii_start, ascii_stop)) for x in xrange(seq_length)]
#    print chromosome
    res = eval_func(chromosome)
    return res

def test_noresults():
    results = test_evalWithRandomValues(10)
    return results

def test_somesults():
    results = test_evalWithRandomValues(0)
    return results

def test_normalresults():
    chromosome = "alternative splicing"
    results = eval_func([x for x in chromosome])
    return results

if __name__ == '__main__':
#    nores = test_noresults()
#    splicing = test_normalresults()

    run()
