#!/usr/bin/env python
"""
"""
import pyevolve
from pyevolve import Consts
import random


class GoogleQueryChromosome(list):
    """
    a list-like object that represents a Google Query
    """
    def __str__(self):
        """
        """
        rep = "Chromosome: "
        rep += ' '.join(list.__repr__(self))
        return rep

class GoogleQueryGenome(pyevolve.GenomeBase.GenomeBase):
    """
    diploid genome, each chromosome is a string.
    """
    evaluator = None
    initializator = None
    mutator = None
    crossover = None

    def __init__(self, seqlength, cloning=False):
       """
       """
       pyevolve.GenomeBase.GenomeBase.__init__(self)
       self.setParams(seqlength = seqlength)
       self.genomeList = [GoogleQueryChromosome([None])*seqlength, GoogleQueryChromosome([None])*seqlength]
#
       if not cloning:
           self.initializator.set(googleQueryInitializer)
#           self.mutator.set(Consts.CDefG2DListMutator)
#           self.crossover.set(Consts.CDefG2DListCrossover)

    def clearList(self):
       self.genomeList = [GoogleQueryChromosome([None])*self.seqlength, GoogleQueryChromosome([None])*self.seqlength]

    def getHeight(self):
        return 2

    def getWidth(self):
        return self.getParam("seqlength")

    def getSize(self):
        return self.getParam("seqlength")

    def setItem(self, x, y, value):
        self.genomeList[x][y] = value

    def __str__(self):
        """
        """
        rep = "CHROMOSOME1: "
        rep += str(self.genomeList[0])
        rep += "CHROMOSOME2: "
        rep += str(self.genomeList[1])
        return (rep)
        
def googleQueryInitializer(genome, **args):
    """
    initialize google query genome
    """
    chr1 = [chr(random.randint(0, 255)) for n in xrange(genome.getParam("seqlength"))]
    chr2 = [chr(random.randint(0, 255)) for n in xrange(genome.getParam("seqlength"))]
    genome.genomeList = [chr1, chr2]



def test():
    pass







if __name__ == '__main__':
    pass

