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

debug = False

# define lower and upper limits for Ascii chars. Extreme values are 0, 255
rangemin = 0
rangemax = 255

# other parameters
seq_length = 500
ngenerations = 10



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
#    print "CHROMOSOME:", chromosome.genomeList, 
    print "CHROMOSOME:",
    genotype = [chr(x) for x in chromosome.genomeList]
    genotype = ''.join(genotype)
    genotype = notalpha_regex.sub(' ', genotype)
    print genotype,
##    print results
##    print_fancy_results(results)
    if debug:
        score = len(re.findall('[\w ]', genotype))
    else:
        results = launch_query(genotype)

        if not results['responseData']['cursor'].has_key('estimatedResultCount'):
            score = 0
        else:
            score = int(results['responseData']['cursor']['estimatedResultCount'])
    print score

#    print chromosome
#    print score
    return score


def run():
    """
    run the pipeline
    """
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
