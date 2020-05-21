import random
import sklearn.datasets

# Squared matrix

# parameters
amount = 5
mn_size = 50
mx_size = 100
rng = [-1000, 1000]


def ordinary_matrix():
    print("ordinary")
    line = ""
    for i in range(mn_size, mx_size + 1):
        for k in range(amount):
            line += str(i) + "\n"
            for rows in range(i):
                for col in range(i):
                    line += str(random.randint(rng[0], rng[1])) + " "
                line += "\n"
    open("input_data/ordinary.txt", "w", encoding="UTF-8").write(line)


def lower_and_upper_triangular_matrix():
    print("traingular")
    line_lower = ""
    line_upper = ""
    for i in range(mn_size, mx_size + 1):
        for k in range(amount):
            line_lower += str(i) + "\n"
            line_upper += str(i) + "\n"
            for rows in range(i):
                for col in range(rows + 1):
                    line_lower += str(random.randint(rng[0], rng[1])) + " "
                    line_upper += "0 "
                for col in range(rows + 1, i):
                    line_lower += "0 "
                    line_upper += str(random.randint(rng[0], rng[1])) + " "
                line_lower += "\n"
                line_upper += "\n"
    open("input_data/lower_triangular.txt", "w", encoding="UTF-8").write(line_lower)
    open("input_data/upper_triangular.txt", "w", encoding="UTF-8").write(line_upper)


def diagonal_and_graph_matrix():
    print("diag")
    line_diagonal = ""
    line_graph = ""
    for i in range(mn_size, mx_size + 1):
        for k in range(amount):
            line_diagonal += str(i) + "\n"
            line_graph += str(i) + "\n"
            for rows in range(i):
                for col in range(rows):
                    line_diagonal += "0 "
                    line_graph += str(random.randint(rng[0], rng[1])) + " "
                line_diagonal += str(random.choice([-1, 1]) * random.randint(1, rng[1])) + " "
                line_graph += "0 "
                for col in range(rows + 1, i):
                    line_diagonal += "0 "
                    line_graph += str(random.randint(rng[0], rng[1])) + " "
                line_diagonal += "\n"
                line_graph += "\n"
    open("input_data/diagonal.txt", "w", encoding="UTF-8").write(line_diagonal)
    open("input_data/graph.txt", "w", encoding="UTF-8").write(line_graph)


def non_and_symmetric_matrix():
    print("symm")
    line_sym = ""
    line_non_sym = ""
    for i in range(mn_size, mx_size + 1):
        for k in range(amount):
            lst_sym = [[0 for _ in range(i)] for _ in range(i)]
            lst_non_sym = [[0 for _ in range(i)] for _ in range(i)]
            line_sym += str(i) + "\n"
            line_non_sym += str(i) + "\n"
            for rows in range(0, i):
                for cols in range(rows, i):
                    lst_sym[rows][cols] = random.randint(rng[0], rng[1])
                    lst_sym[cols][rows] = lst_sym[rows][cols]
                    lst_non_sym[rows][cols] = random.randint(rng[0], rng[1])
                    lst_non_sym[cols][rows] = -lst_non_sym[rows][cols]
            for ln in lst_sym:
                for num in range(0, len(ln) - 1):
                    line_sym += str(ln[num]) + " "
                line_sym += str(ln[-1]) + "\n"
            for ln in lst_non_sym:
                for num in range(0, len(ln) - 1):
                    line_non_sym += str(ln[num]) + " "
                line_non_sym += str(ln[-1]) + "\n"
    open("input_data/symmetric.txt", "w", encoding="UTF-8").write(line_sym)
    open("input_data/non_symmetric.txt", "w", encoding="UTF-8").write(line_non_sym)


def sparsity_matrix():
    print("sparsity")
    line = ""
    for i in range(mn_size, mx_size + 1):
        for k in range(amount):
            line += str(i) + "\n"
            for rows in range(0, i):
                for cols in range(0, rows):
                    if random.random() > 0.8:
                        line += str(random.randint(rng[0], rng[1])) + " "
                    else:
                        line += "0 "
                line += str(random.choice([-1, 1]) * random.randint(1, 1000)) + " "
                for cols in range(rows + 1, i):
                    if random.random() > 0.95:
                        line += str(random.randint(rng[0], rng[1])) + " "
                    else:
                        line += "0 "
                line += "\n"
    open("input_data/sparsity.txt", "w", encoding="UTF-8").write(line)


def symmetric_positive_definite():
    print("spd")
    line = ""
    for i in range(mn_size, mx_size + 1):
        for k in range(amount):
            line += str(i) + "\n"
            b = sklearn.datasets.make_sparse_spd_matrix(i)
            for row in b:
                for el in row:
                    line += str(int(el)) + " "
                line += "\n"
    open("input_data/symm_pos_def.txt", "w", encoding="UTF-8").write(line)


ordinary_matrix()
lower_and_upper_triangular_matrix()
diagonal_and_graph_matrix()
non_and_symmetric_matrix()
sparsity_matrix()
symmetric_positive_definite()
