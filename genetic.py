from random import randint, choice, random, choices
import time

lowercase = "abcdefghijklmnopqrstuvwxyz "

#fitnessEmphasis = 2 # if fitnessEmphasis = 2, then a string with fitness of 5 has 2x more chance of reproducing than a string with a fitness of 4.
fitnessEmphasis = 2

# .05 means a 5% mutation rate
mutationRate = .05

mostFitDNA = "to be or not to be"

# https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice

class Organism:
    """ Organism """
    def __init__(self, DNA):
        self.DNA = DNA
        self.fitness = self.compute_fitness()

    def __str__(self):
        return self.DNA

    def compute_fitness(self):
        """ Computes the organism's fitness. """
        score = 0
        for index in range(len(mostFitDNA)):
            if self.DNA[index] == mostFitDNA[index]:
                score += 1
        return score

def main():
    btime = time.time()
    parentPool = []
    childPool = []
    genNum = 0
    # Generate the initial list of Organisms
    for x in range(2):
        parentPool.append(Organism(randomword(len(mostFitDNA))))

    mostFitFound = False

    while not mostFitFound:
        for y in range(2):
#                    if score == len(mostFitDNA):
#            print("Found it! " + self.DNA)
#            notFoundMostFit = False
            child = select_mate(parentPool)

            if child.fitness == len(mostFitDNA):
                #print("Found it! " + child.DNA)
                for elem in childPool:
                    print(elem)

                print("Found it! " + child.DNA)
                etime = time.time()
                print(etime-btime)
                mostFitFound = True
                break

            childPool.append(child)
        # Clear the parentPool to load in the childPool. Then clear the childPool.
        parentPool.clear()
        parentPool = list(childPool)
        childPool.clear()
        genNum += 1
        #print(genNum)

def randomword(length):
   return ''.join(choice(lowercase) for i in range(length))


def select_mate(genePool):
    """ Selects two strings and mates them out of the entire genePool to output a new Organism """
#    # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
#
#    mates = []
#    # Select two mates from the gene pool
#    while True:
#        a = choice(genePool)
#
#        # select the mates by using the following fitness function
#        if random() < 1 / (fitnessEmphasis ** (len(mostFitDNA) - a.fitness)):
#            mates.append(a)
#        if len(mates) == 2:
#            break
#
#    # Call reproduce to produce a new Organism
#    return reproduce(mates[0], mates[1])
    weights = []
    totalWeights = 0

    # Formulate the value for totalWeights, so that the values in weights adds to 1
    for org in genePool:
        totalWeights += 2 ** org.fitness

    #print(totalWeights)
    # Create the list of how each organism is weighted
    for org in genePool:
        weights.append(2 ** org.fitness / totalWeights)
        #print(2 ** org.fitness / totalWeights)

    # Pick two organisms from the gene pool, by weights, to mate.
    mate1 = choices(genePool, weights, k=1)
    mate2 = choices(genePool, weights, k=1)
    return reproduce(mate1[0], mate2[0])

def reproduce(a, b):
    # http://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
    """returns a random offspring generated from the inputted parents"""

    # Needs to do mutations. Work on mutations later.########################################
    x = randint(0,len(mostFitDNA))

    # Figure out the new DNA
    DNA = a.DNA[:x] + b.DNA[x:]

    # Mutation Code
    if random() < mutationRate:
        # If there is a mutation, then give put in a lowercase letter somewhere random
        x = randint(0,len(mostFitDNA))

        # Insert the letter into the xth position of the DNA
        if (x < len(mostFitDNA)):
            DNA = DNA[:x] + choice(lowercase) + DNA[x+1:]
        else:
            DNA = DNA[:x-1] + choice(lowercase)

    # Make an organism with the specified DNA
    return Organism(DNA)

if __name__ == "__main__":
    main()