The Genetics of a Google Query Population
=========================================

This is a spare-time project of mine, an extension to an exercise I did back at
the UNI.

The idea is to evaluate the efficiency of the tests used by the scientific
community to detect traces of positive selection on genotype data, by applying
them to the results of a genetic algorithm.

I could not come out with a nice application of genetics algorithms, so I
figured out to create a GA to get the google query with the highest number of
results.

How does it work
------------------

* the GA will generate a number of random sequences of words, of the same length. These will correspond to the genome of different individuals. Example:

    Ind1: cas jho jo ckasc pacpcppp oasa dlaskd q 

    Ind2: hhasd j aj aosk ala mcalkxcn lal lsalsa 

    Ind3: jaj  nasod mnlas lw q  jj j jdsjai oocvo

* the GA program will evolve these series of letters by introducing random puntiform mutations (changing a single letter) and crossing overs. The fitness of each individual will be the number of results it gets when called on google. This phase is equivalent to the primordial phase of the world, when molecules of RNA started appearing giving birth to different forms of organisms.


* After a certain number of generations, I expect some words to emerge from the chaos. In principle these words should give a good boost to the score of a query on google, therefore enhancing its fitness and making it more likely to survive. This phase is similar to when the first forms of life appeared on the Earth; not all the forms of life that could have appeared have emerged, and in the same way, not all the words that exist will appear in that phase.

* After other generations, I expect only few kinds of words to resist. This will be similar to different species that can merge together. This phase will be good to test PAML and other similar packages

* Toward the end of the simulation, I expect queries to not change very much; only a few positions will be variable. This will be similar to having SNPs on a population of individuals in a specie, and will be good to test iHS and similar statistics.
