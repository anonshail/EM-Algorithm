# Introduction
The given code is the implementation of the EM Algorithm which estimates the bias of two coins. EM algorithm is used to label data which is unlabeled based only on 
the data itself. 

# How does the EM algorithm work in the case of the coin flipping experiment?
The EM algorithm helps us determine which coin is being used by starting with a guess for the coin biases. Initially, a random value is assigned, which then helps us estimate which coin was chosen in each trial as we can calculate the approximate value of the expected number of heads and tails for each coin. This constitutes the “E-Step” of the algorithm. By using these counts, we can recompute the bias of each coin, which is known as the “M-Step”. By iteratively repeating these two steps, we can refine the value of the biases of the coin till they eventually converge. Hence, we are able to calculate the bias of a coin based on nothing but the data itself, and we are able to assign a label to the given data.

# Code choices for implementation of EM Algorithm
1. Number of iterations to approximate the bias of the coin: In the current implementation, 20 iterations are made to obtain an accurate value of the bias of each coin. Although 5 iterations would suffice till the values converge, since there is no limiting factor and the runtime for 20 iterations isn’t large, 20 iterations are used in the interest of obtaining more accurate values.
2. The choice of datatype to handle the data: To store the coin data, the current implementation makes use of a 2D 30x20 list for 30 coin draws. Since this would be the easiest way to maintain and iterate over the data, a 2D list was chosen for the job.
3. Another choice faced is the degree of modularity of code. The implementation is broken up into multiple functions to keep the flow of logic clean and easy to comprehend. This helps with debugging and figuring out issues with code, and this also helps if another developer were to contribute or expand upon the current implementation, as the code becomes more readable.


