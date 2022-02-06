# Evolutionary Computing Algorithms

## Table of Contents
1. [Generating Initial Populations](GeneratingInitialPopulations.ipynb)
2. [Genetic Algorithms](GeneticAlgorithms.ipynb)


Evolutionary Computation (EC) is a sub-field of computational intelligence that deals with several computational techniques which are based to some degree on the evolution of biological life in the natural world. These computational techniques use computational models of evolutionary processes, such as: natural selection, survival of the fittest and reproduction, as the fundamental components of such computational systems. Evolutionary techniques mostly involve metaheuristic optimization algorithms such as evolutionary algorithms (comprising genetic algorithms, evolutionary programming, evolution strategy, genetic programming and learning classifier systems) and swarm intelligence (comprising ant colony optimization and particle swarm optimization). 

The most widely used form of evolutionary computation are Genetic Algorithms (GA). GA is an adaptive heuristic search algorithm that is designed to simulate processes in natural system necessary for evolution proposed by Charles Darwin. This algorithm represents an intelligent exploitation of a random search within a defined search space to solve a problem. The first GA was developed by Holland in 1975, referred to as Simple Genetic Algorithm (SGA). It also sometimes referred to as the classical or canonical GA. Real-valued GA and Permutations GA are other variants of GA. 

GAs handle a population of individuals (solutions). The probability of selecting a bad solution is reduced by handling multiple good solutions.  The population evolves from one iteration to the next according to selection and the search operators (genetic operators).

[Simulated Annealing (SA)](../TrajectoryAlgorithms/SimulatedAnnealing.ipynb) can be thought of as GA where the population size is only one. The current solution is the only individual in the population. 
As there is only one individual, there is no crossover, but only mutation. As a matter of fact this is the primal difference between SA and GA. 
SA produces a new solution by changing only one solution with a local move, while GA produces solutions by fusing two different solutions.