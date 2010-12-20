#!/usr/bin/env python
"""
main pipeline for the Genetic Algorithm
"""


import pyevolve as pv
from pyevolve import GSimpleGA
from pyevolve import G1DList
from launch_query import launch_query, print_fancy_results
import random
import re

# define lower and upper limits for Ascii chars. Extreme values are 0, 255
ascii_start = 0
ascii_stop = 255

# other parameters
seq_length = 500


notalpha_regex = re.compile('\W')

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
    print "CHROMOSOME:", chromosome
    chromosome = ''.join(chromosome)
    chromosome = notalpha_regex.sub(' ', chromosome)
##    print chromosome
#    results = launch_query(chromosome)
##    print results
##    print_fancy_results(results)

    score = random.randrange(100)

#    if not results['responseData']['cursor'].has_key('estimatedResultCount'):
#        score = 0
#    else:
#        score = results['responseData']['cursor']['estimatedResultCount']
#
#    print chromosome
#    print score
    return score


def run():
    """
    """
    genome = G1DList.G1DList(20)
    genome.evaluator.set(eval_func)
    ga = GSimpleGA.GSimpleGA(genome)
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
