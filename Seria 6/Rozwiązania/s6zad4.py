

import numpy as np

# R - położenia czastek na osi X
# Q - ładunki czastek 
R = np.array([1,2,4])
Q = np.array([1, -1, 2])

#Chcemy rozwiazac zadanie bez pętli, co oczywiście jest możliwe
# Tworzymy macierz R_mat, której elementy R_ij oznaczaja różnicę 
# odległości między czastka i oraz j.
R_mat = R[:,np.newaxis] - R[np.newaxis,:]
Q_mat = Q[:,np.newaxis] * Q[np.newaxis,:]

dist = np.abs(R_mat)
dist[dist == 0] = 1


F = R_mat/dist**3 * Q_mat

F_values = np.sum(F, axis = 1)

