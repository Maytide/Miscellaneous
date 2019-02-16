# Doubly Stochastic Matrices as Convex Combinations of Permutation Matrices: A Linear Programming Approach

[Source.](https://math.stackexchange.com/questions/214948/whats-the-algorithm-of-finding-the-convex-combination-of-permutation-matrices-f?rq=1)

Paraphrasing the source, it has been shown previously that n-ny-n doubly stochastic matrices can be written as a convex combination of n-by-n permutation matrices. This repo gives a linear programming algorithm to determine this convex combination. However, the solution is pretty inefficient: it requires storing each permutation matrix in memory. The number of possible permutation matrices grows by n!, and the size of each matrix grows by n^2.

Currently, it doesn't exploit the doubly stochastic structure. But I think it's possible to reduce memory usage by something like a factor of n if this information is used.