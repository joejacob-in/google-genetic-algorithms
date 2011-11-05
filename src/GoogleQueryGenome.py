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
    chr1 = [chr(random.randint(30, 126)) for n in xrange(genome.getParam("seqlength"))]
    chr2 = [chr(random.randint(30, 126)) for n in xrange(genome.getParam("seqlength"))]
#    chr1 = [chr(random.randint(0, 255)) for n in xrange(genome.getParam("seqlength"))]
#    chr2 = [chr(random.randint(0, 255)) for n in xrange(genome.getParam("seqlength"))]
    genome.genomeList = [chr1, chr2]


def googleQueryMutator(genome, **args):
   """ The mutator of GoogleQueryChromosome
   
   """
   
   print "Mutating genome", genome
   if args["pmut"] <= 0.0: return 0
#   height, width = genome.getParam('seqlength')
   height = 2
   width = genome.getParam('seqlength')
   elements = height * width

   mutations = args["pmut"] * elements

   if mutations < 1.0:
      mutations = 0
   for i in xrange(height):
      for j in xrange(width):
         if Util.randomFlipCoin(args["pmut"]):
             index_b = (random.randint(0, height-1), random.randint(0, width-1))
             list2DSwapElement(genome.genomeList, (i,j), index_b)
             mutations+=1
   else:
      for it in xrange(int(round(mutations))):
         index_a = (random.randint(0, height-1), random.randint(0, width-1))
         index_b = (random.randint(0, height-1), random.randint(0, width-1))
         Util.list2DSwapElement(genome.genomeList, index_a, index_b)

   return int(mutations)

def list2DSwapElement(lst, indexa, indexb):
   """ Swaps elements A and B in a 2D list (matrix).

   Example:
      >>> l = [ [1,2,3], [4,5,6] ] 
      >>> Util.list2DSwapElement(l, (0,1), (1,1) )
      >>> l
      [[1, 5, 3], [4, 2, 6]]

   :param lst: the list
   :param indexa: the swap element A
   :param indexb: the swap element B
   :rtype: None

   """
   temp = lst[indexa[0]][indexa[1]]
   lst[indexa[0]][indexa[1]] = lst[indexb[0]][indexb[1]]
   lst[indexb[0]][indexb[1]] = temp


def test():
    pass







if __name__ == '__main__':
    pass

