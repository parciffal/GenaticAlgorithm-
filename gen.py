from random import randint

s = 'abcdefghijklmnopqrstuvwxyz'

# Simple genetic algorithm thet learns how to write a correct word


def rem(word: str):
    ill = []

    for w in word:
        for i in range(len(s)):
            if w == s[i]:
                print(i)
                ill.append(i)
    return ill


def mer(ill: list):
    idd = []
    for i in ill:
        idd.append(s[i])
    return idd


class GeneticAlgorithm:

    def __init__(self, word, chromosome_number, mutation_chance, limit):
        gene_number = len(word)
        l = self.initialize_population(gene_number, chromosome_number)
        print('Start : ')
        for i, chromosome in enumerate(l):
            print(f'#{i} {chromosome} summ : {mer(chromosome)}')

        l = self.fitness(l, word)
        for i_to_limit in range(limit):
            _l = self.crossover(l)
            _l = self.mutation(_l, mutation_chance)
            _l = self.fitness(_l, word)
            l = _l
        print('Result : ')
        for i, chromosome in enumerate(l):
            print(f'#{i} {chromosome} summ : {mer(chromosome)}')

    def initialize_population(self, gene_number, chromosome_number):
        """
        Initializing population to work with
        :return: list with population (Chomosomes and genes)
        """
        l = []
        for chromosome in range(chromosome_number):
            l.append([])
            for gene in range(gene_number):
                l[-1].append(randint(0, 25))
        return l

    def fitness(self, l, word):
        """
        It is vitally important function, which defines are parameters
        fit or not for the solution
        :param l: list with  population
        :return: probability that individual will be selected for further reproduction
        """
        b = rem(word)
        maxApp = 0
        values = {}
        for i, chromosome in enumerate(l):
            _summ = 0
            for j in range(len(word)):
                if chromosome[j] == b[j]:
                    _summ += 1
                    print(chromosome[j], b[j])
                else:
                    chromosome[j] = randint(0, 25)
            if _summ > maxApp:
                maxApp = _summ

            values[i] = _summ
            print(chromosome, ';', str(_summ), mer(chromosome))
        _values = []
        for i in values:
            if values[i] >= maxApp:
               _values.append(i)

        _l = []
        for index in _values:
            _l.append(l[index])
        if len(_l) == 1:
            _l.append(l[-1])

        return _l

    def crossover(self, l):
        """
        Get all off-springs  (population size = a(i) ... a(i+1) )
        Here we use 'One Point Crossover'
        :return: new l
        """
        _l = []
        for i, chromosome_i in enumerate(l):
            for j in range(i + 1, len(l)):
                parent_1 = l[i]
                parent_2 = l[j]
                new_parent_1_left = l[i][:len(l[i]) // 2]
                new_parent_1_right = l[j][len(l[i]) // 2:]
                new_parent_2_left = l[j][:len(l[j]) // 2]
                new_parent_2_right = l[i][len(l[j]) // 2:]
                new_parent_1 = []
                new_parent_1.extend(new_parent_1_left)
                new_parent_1.extend(new_parent_1_right)
                new_parent_2 = []
                new_parent_2.extend(new_parent_2_left)
                new_parent_2.extend(new_parent_2_right)
                _l.append(new_parent_1)
                _l.append(new_parent_2)

        return _l

    def mutation(self, _l, mutation_chance):
        """
        For some chromosomes add mutation
        :return: list with mutated chromosomes
        """

        mutation_chance = mutation_chance * 100
        for i, chromosome in enumerate(_l):
            if randint(0, 100) <= mutation_chance:
                # mutate
                _l[i][randint(0, len(chromosome)) - 1] = randint(0, 25)

        return _l


import time
word = input("Enter word:")
start = time.perf_counter()
GeneticAlgorithm(chromosome_number=50, mutation_chance=0.01, limit=100, word=word)
print(f'finished in {round(time.perf_counter() - start)} sec')
