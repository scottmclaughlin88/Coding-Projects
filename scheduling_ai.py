#You don't know what the end goal is, but you are trying to perfect and reach it.
#E.g. Best path to travel, between lots of cities.

#Try to convert a string of 1's to 0's.
#Score it based on the difference of 1's to 0's.
import random
from time import time

#https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters-in-p
#the *args will give you all function parameters as a tuple:
#The **kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary.
#Useful for timing a function in a script.
def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

#Score each individual.
def score(individual):
    fitness = 0
    fitness += score_distribution(individual)
    fitness += score_overlapping(individual)
    return fitness

#Mutate new individuals.
def mutate(individual):
    offspring = {}
    for key,value in individual.items():
        if random.randint(0, 3) == 0:
            change = random.randint(-2, 2)
            offspring[key] = value + change
        else:
            offspring[key] = value
    return offspring

#Get list of fittest individuals of population.
def get_fittest(population):
    best_score = -1000
    best_individual = None
    for individual in population:
        if score(individual) > best_score:
            best_score = score(individual)
            best_individual = individual
    return best_individual

#Print the current population.
def print_population(population):
    print('\nCurrent pop')
    for individual in population:
        print(individual)

#Generate population.
def generate_population(individual):
    population = []
    for x in range(10):
        population.append(mutate(individual))
    population.append(individual)
    return population

#Deduct points for schedules that critical or severe appointments close to other appointments.
def score_distribution(individual):
    fitness = 0
    if abs(individual['Severe'] - individual['Critical']) <= 1:
        fitness -= 10
    if abs(individual['Severe'] - individual['Neutral']) <= 1:
        fitness -= 5
    if abs(individual['Severe'] - individual['Medium']) <= 1:
        fitness -= 2.5
    if abs(individual['Severe'] - individual['Normal']) <= 1:
        fitness -= 1

    if abs(individual['Critical'] - individual['Neutral']) <= 1:
        fitness -= 3
    if abs(individual['Critical'] - individual['Medium']) <= 1:
        fitness -= 1.5
    if abs(individual['Critical'] - individual['Normal']) <= 1:
        fitness -= 0.5
    return fitness

def score_overlapping(individual):
    fitness = 0
    all_values = individual.values()
    no_dupes = set(all_values)
    dupes = (len(all_values) - len(no_dupes))
    fitness -= dupes * 20
    return fitness

#5 different appointments, with a unique name.  A-F, and the hour they start
adam = {'Normal': 0, 'Medium': 0, 'Neutral': 0, 'Critical': 0, 'Severe': 0}
best_score = score(adam)
generation = 0
population = [adam]

while best_score < 0:
    print_population(population)
    fittest = get_fittest(population)
    # print('best: ', fittest)
    population = generate_population(fittest)
    generation += 1
    print(f'Gen {generation} current fittest {fittest} with a score of {score(fittest)}')
    best_score = score(fittest)