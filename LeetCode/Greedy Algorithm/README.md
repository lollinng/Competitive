greedy algorithm is a very natural solution for problems that it can solve, and any usage of dynamic programming will end up to be “overkill”.
We find a rule, sort the items by some type of ordering — time, distance, size, or some type of ration, and we construct our optimal solutions incrementally w/o considering preceding items or choices incrementally and we end up having our optimal solution

We can try the following six steps to solve a problem which can be potentially solved by making greedy choice:
1)Divide the problem into subproblems, including one small problem and the remaining subproblem.
2)Determine the optimal substructure of the problems (formulating a recurrence function).
3)Show that if we make the greedy choice, then only one subproblem remains.
4)Validate the rightness of the greedy choice.
5)Write either a recursive or an iterative implementation.

When to use it ?
Whenever we see optimum or maximum or minimum or larget or smallest, the first approach which should strike our mind should be Greedy or Dynamic Programming. If the problem is solvable via recursion, one should do for memoized recursion or DP else start with the brute force and reduce it to Greedy.

