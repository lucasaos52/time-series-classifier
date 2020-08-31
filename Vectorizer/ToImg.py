import sys
import numpy as np

# converte série temporal (Z,K) onde Z = Numero de timesteps e K = numero de amostras 
# em uma matrix M X N.
class ToImg:
    def __init__(self, m=5, n=5):
        self.m = m
        self.n = n
  	    
    def train(self, x_trains, y_trains):
        best_m, best_n = self.step1(x_trains, y_trains)
        best_m, best_n = self.step2(x_trains, y_trains, best_m, best_n)
        self.m = best_m
        self.n = best_n
 	
    def dataset_to_matrix(self, ts_set):
        matrices = []
        for ts in ts_set:
            matrices.append(self.ts_to_img(ts))

        return np.array(matrices)
 	 	
    def ts_to_img(self, ts):
        matrix = np.zeros((self.m, self.n))
        T = len(ts)

        height = 1.0/self.m
        width = T/self.n

        for idx in range(T):
            i = int((1-ts[idx])/height)
            if i == self.m:
                i -= 1

            t = idx+1
            j = t/width
            if int(j) == round(j, 7):
                j = int(j)-1
            else:
                j = int(j)

            matrix[i][j] += 1
        return matrix
