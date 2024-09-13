from population import PopulationClass
from chromosome import ChromosomeClass

def print_population(population: list[ChromosomeClass]):
    for chromossome in population:
        print_chromossome(chromossome)

def print_chromossome(chromossome: ChromosomeClass, show_fitness: bool = False):
    for c in chromossome.value:
        print(chr(c), end=" ")
    if(show_fitness): print(" = ", chromossome.fitness)
    else: print()

def print_stats(population: PopulationClass, generation: int):
    print(f"Generation {generation} / Average fitness: {sum([c.fitness for c in population.population]) / len(population.population)}: ")
    print(f"Best -> ", end="")
    print_chromossome(population.population[0], True)
    print(f"Worst -> ", end="")
    print_chromossome(population.population[-1], True)
    print()
