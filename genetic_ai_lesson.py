#You don't know what the end goal is, but you are trying to perfect and reach it.
#E.g. Best path to travel, between lots of cities.

#Try to convert a string of 1's to 0's.
#Score it based on the difference of 1's to 0's.
import random
from time import time

#Useful for timing a function in a script
def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def score(individual):
    fitness = 0
    for gene in individual:
        if gene == 1:
            fitness += 1
    return fitness

#Mutate new individuals
def mutate(individual):
    offspring = []
    for gene in individual:
        if random.randint(0, 3) == 0:
            if gene == 1:
                offspring.append(0)
            else:
                offspring.append(1)
        else:
            offspring.append(gene)
    return offspring

#Get list of fittest individuals of population
def get_fittest(population):
    best_score = -1
    best_individual = None
    for individual in population:
        if score(individual) > best_score:
            best_score = score(individual)
            best_individual = individual
    return best_individual

def print_population(population):
    print('\nCurrent pop')
    for individual in population:
        print(individual)

#Generate population
def generate_population(individual):
    population = []
    for x in range(10):
        population.append(mutate(individual))
    population.append(individual)
    return population
    

adam  = [0, 0, 0, 0]
print_score = 0
generation = 0
population = [adam]

while print_score < 4:
    print_population(population)
    fittest = get_fittest(population)
    # print(fittest)
    population = generate_population(fittest)
    generation += 1
    print(f'Gen {generation} current fittest {fittest} with a score of {score(fittest)}')
    print_score = score(fittest)

