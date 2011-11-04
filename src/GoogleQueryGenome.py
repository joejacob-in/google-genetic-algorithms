#!/usr/bin/env python
"""
"""
import pyevolve
from pyevolve import Consts, Util
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
           self.mutator.set(googleQueryMutator)
#           self.crossover.set(Consts.CDefG2DListCrossover)

    def clearList(self):
       self.genomeList = [GoogleQueryChromosome([None])*self.seqlength, GoogleQueryChromosome([None])*self.seqlength]

    def getHeight(self):
        return 2

    def getWidth(self):
        return self.getParam("seqlength")

    def getSize(self):
        return (2, self.getParam("seqlength"))

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


def googleQueryMutator(genome, **args):
   """ The mutator of G1DList, Swap Mutator
   
   .. note:: this mutator is :term:`Data Type Independent`

   """
   
   if args["pmut"] <= 0.0: return 0
   height, width = genome.getSize()
   elements = height * width

   mutations = args["pmut"] * elements

   if mutations < 1.0:
      mutations = 0
      for i in xrange(height):
         for j in xrange(width):
            if Util.randomFlipCoin(args["pmut"]):
               index_b = (rand_randint(0, height-1), rand_randint(0, width-1))
               Util.list2DSwapElement(genome.genomeList, (i,j), index_b)
               mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         index_a = (rand_randint(0, height-1), rand_randint(0, width-1))
         index_b = (rand_randint(0, height-1), rand_randint(0, width-1))
         Util.list2DSwapElement(genome.genomeList, index_a, index_b)

   return int(mutations)

def test():
    pass







if __name__ == '__main__':
    pass

