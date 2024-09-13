import random
from chromosome import ChromosomeClass

class PopulationClass:
  population: list[ChromosomeClass] = []
  best_fitness: float = 0.0

  def __init__(self):
    pass

  def populate(self, objective_length: int, population_length: int) -> list[ChromosomeClass]:
    if self.population is None or self.population == []:
      for _ in range(population_length):
        temp = [random.randint(65, 90) for __ in range(objective_length)]
        self.population.append(ChromosomeClass(temp))
      
      return self.population

  def sort_population(self) -> list[ChromosomeClass]:
    self.population = sorted(self.population, key=lambda x: x.fitness, reverse=True)
    self.population[0].fitness = self.best_fitness
    return self.population