import numpy as np
import time
import algorithms
from scipy import linalg
from to_two_dimentional_arr import to_arr


class Tester:
    def __init__(self):
        self.times = {}
        self.types = ["ordinary", "lower_triangular", "upper_triangular", "diagonal", "graph", "symmetric",
                      "non_symmetric", "sparsity"]
        self.methods = [self.qr, self.lu, self.svd]

    def qr(self, matrix, b):
        q, r = linalg.qr(matrix)
        y = np.dot(q.T, b)
        try:
            x = linalg.solve(r, y)
        except:
            pass

    def qr_pure(self, matrix, b):
        q, r = algorithms.qr_pure(matrix)
        y = np.dot(q, b)
        try:
            x = linalg.solve(r, y)
        except:
            pass

    def lu(self, matrix, b):
        lu = linalg.lu_factor(matrix)
        try:
            x = linalg.lu_solve(lu, b)
        except:
            pass

    def lu_pure(self, matrix, b):
        lu = algorithms.lu_pure(matrix)

        x = linalg.lu_solve(lu, b)


    def svd(self, matrix, b):
        u, s, v = linalg.svd(matrix)
        c = np.dot(u.T, b)
        w = linalg.solve(np.diag(s), c)
        x = np.dot(v.T, w)

    def cho(self, matrix, b):
        cho = linalg.cho_factor(matrix)
        x = linalg.cho_solve(cho, b)

    def cho_pure(self, matrix, b):
        cho = algorithms.cholesky_pure(matrix)
        x = linalg.cho_solve(cho, b)

    def test(self):
        for m_type in self.types:
            matrices = to_arr("input_data/" + m_type + ".txt")
            dct = {}
            for method in self.methods:
                res = []
                for m in matrices:
                    start = time.time()
                    method(m, [1 for i in range(len(m))])
                    end = time.time()
                    res.append(round((end - start), 4))
                dct[method.__name__] = res
            self.times[m_type] = dct
        # symmetric positive definite
        symm_pos_def = to_arr("input_data/symm_pos_def.txt")
        s_dct = {}
        for method in self.methods + [self.cho]:
            res = []
            for m in symm_pos_def:
                start = time.time()
                method(m, [1 for i in range(len(m))])
                end = time.time()
                res.append(round((end - start), 4))
            s_dct[method.__name__] = res
        self.times["symmetric_positive_definite"] = s_dct
        return self.times


a = Tester()

times = a.test()

with open("results_full.txt", 'w') as f:
    f.write(str(times))

