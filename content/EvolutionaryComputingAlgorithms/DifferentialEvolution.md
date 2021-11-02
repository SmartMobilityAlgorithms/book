# Differential Evolution

Differential evolution (DE) is a population-based metaheuristic used to solve global optimization problems. It approximates the actual global optimum by iteratively mutating and improving the candidate solutions from the initial ones.  
The DE method cannot guarantee the global optimum is found. The best solution returns depending on the choice of the DE settings as well as the problem itself. 

The differential evolution solver has the following input solutions:
- **Population size**:  is the number of sets of candidate solutions that the solver calculates at each loop iteration in the search process. This size also indicates the number of objective function calls at each loop iteration in the optimization process. A larger population size usually results in better optimization results and a longer execution time. 
- **Scale factor**: is the diversity factor that the solver uses to generate mutant solutions. Larger values of scale factor result in more diverse mutant solutions.
- **Crossover probability**: is the probability that the solver inherits the trial solutions from the mutant solutions. A larger value of crossover probability results in a higher probability that the solver accepts the mutant solutions.
- **Bounds**: contains the upper and lower numeric limits for the solutions being optimized.
- **Objective function definitions**: Contain the implementation of the objective functions that the solver will run to minimize, by optimizing over the decision variables affecting those objective functions.

TBD…
