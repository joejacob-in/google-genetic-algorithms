#!/usr/bin/env python
"""
main pipeline for the Genetic Algorithm
"""


import pyevolve as pv
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
    chromosome = ''.join(chromosome)
    chromosome = notalpha_regex.sub(' ', chromosome)
    print chromosome
    results = launch_query(chromosome)
    print results
    print_fancy_results(results)

    return results


def test_evalWithRandomValues(seed):
    """
    if random.seed(0), this test should return something
    if random.seed(10), this test should return no results
    """
    random.seed(seed)
    chromosome = [chr(random.randrange(ascii_start, ascii_stop)) for x in xrange(seq_length)]
    print chromosome
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
    nores = test_noresults()
    splicing = test_normalresults()

