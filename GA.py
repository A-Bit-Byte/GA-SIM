import simpy
import pandas as pd
import itertools as it
import numpy as np
import random
from dataclasses import dataclass, field
from typing import List
import tabulate


@dataclass
class Individual:
    chromosome: list
    fitness: int = 100

    def __str__(self):
        return self.chromosome


class Population:

    def __init__(self, population_size, number_of_genes):
        self.population_size = population_size

        gene_numeric_values: list = list(range(0, 10))
        gene_conditional_values = ['=', '>', '<']
        gene_variables = ['x', 'y', 'z']

        self.genome = list(it.product(gene_variables, gene_conditional_values, gene_numeric_values))
        self.number_of_genes = number_of_genes
        self.population_list = self.create_population()

    def create_population(self):
        pop = []
        for _ in range(0, self.population_size):
            pop.append(Individual(fitness=random.randint(10, 100),
                                  chromosome=random.choices(self.genome, k=self.number_of_genes)))
        return pop

    def mutate(self, percentage_to_mutate, mutation_rate):
        number_to_mutate = int(self.population_size * percentage_to_mutate)
        mutate_index = random.choices(range(0, self.population_size), k=number_to_mutate)
        for first_index in mutate_index:
            for second_index, g in enumerate(self.population_list[first_index].chromosome):
                if mutation_rate > (random.randint(0, 100) / 100):
                    self.population_list[first_index].chromosome[second_index] = random.choice(self.genome)

    def mate(self, percentage_to_mate):
        self.sort_by_fitness()
        best_25 = int(self.population_size * 0.25)



    def sort_by_fitness(self):
        self.population_list.sort(key=lambda x: x.fitness)

    def __str__(self):
        return tabulate.tabulate([(x.fitness, x.chromosome) for x in self.population_list],
                                 headers=['Fitness', 'Chromosome'], tablefmt='github')


def main():
    pop = Population(10, 8)
    print(pop)
    pop.mutate(0.5, 0.99)
    print("Mutating")
    print(pop)
    print("Mating")
    pop.mate(0.5)
    print(pop)


if __name__ == '__main__':
    main()
