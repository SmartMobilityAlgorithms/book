
# Graph Search

`Searching` is the systematic examination of states to find a path from the start state to the goal state. 

Search algorithms can be broadly classified into `deterministic` algorithms and `stochastic` algorithms. 

In the former, the search algorithm follows a rigorous procedure and its path and values of both design variables and the functions are repeatable. For the same starting point, the algorithm will follow the same path whether you run the program today or tomorrow. 

In the latter, the algorithm always has some randomness and the solution is not exactly repeatable. Based on the availability of information about the search space (e.g. the distance from the current state to the goal), deterministic search algorithms can be broadly classified into `blind/uninformed` and `informed` search.

![Graph Search](../../images/GraphSearch.png)