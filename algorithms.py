import copy
from math import sqrt


def mult_matrix(M, N):
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in N] for row_m in M]


def pivot_matrix(M):
    m = len(M)
    id_mat = [[float(i == j) for i in range(m)] for j in range(m)]
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]
    return id_mat


def lu_pure(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    P = pivot_matrix(A)
    PA = mult_matrix(P, A)
    for j in range(n):
        L[j][j] = 1.0
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]
    return (P, L, U)


def trans_matrix(M):
    n = len(M)
    return [[M[i][j] for i in range(n)] for j in range(n)]


def norm(x):
    return sqrt(sum([x_i ** 2 for x_i in x]))


def Q_i(Q_min, i, j, k):
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i - k][j - k]


def cmp(a, b):
    return (a > b) - (a < b)


def qr_pure(A):
    n = len(A)
    R = copy.copy(A)
    Q = [[0.0] * n for i in range(n)]
    for k in range(n - 1):
        I = [[float(i == j) for i in range(n)] for j in range(n)]
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in I[k:]]
        alpha = -cmp(x[0], 0) * norm(x)
        u = list(map(lambda p, q: p + alpha * q, x, e))
        norm_u = norm(u)
        v = list(map(lambda p: p / norm_u, u))
        Q_min = [[float(i == j) - 2.0 * v[i] * v[j] for i in range(n - k)] for j in range(n - k)]
        Q_t = [[Q_i(Q_min, i, j, k) for i in range(n)] for j in range(n)]
        if k == 0:
            Q = Q_t
            R = mult_matrix(Q_t, A)
        else:
            Q = mult_matrix(Q_t, Q)
            R = mult_matrix(Q_t, R)
    return trans_matrix(Q), R


def cholesky_pure(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            if (i == k):
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
