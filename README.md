#Introduction
The given code is the implementation of the EM Algorithm which estimates the bias of two coins. EM algorithm is used to label data which is unlabeled based only on 
the data itself. 

#How does the EM algorithm work in the case of the coin flipping experiment?
The EM algorithm helps us determine which coin is being used by starting with a guess for the coin biases. Initially, a random value is assigned, which then helps us estimate which coin was chosen in each trial as we can calculate the approximate value of the expected number of heads and tails for each coin. This constitutes the “E-Step” of the algorithm. By using these counts, we can recompute the bias of each coin, which is known as the “M-Step”. By iteratively repeating these two steps, we can refine the value of the biases of the coin till they eventually converge. Hence, we are able to calculate the bias of a coin based on nothing but the data itself, and we are able to assign a label to the given data.
