def to_arr(name):
    file = open(name, 'r', encoding="UTF-8")
    lines = file.readlines()
    i = 0
    matrices = []
    while i != len(lines):
        size = int(lines[i])
        i += 1
        matrix = []
        for k in range(i,i + size):
            matrix.append(list(map(int, lines[k].split())))
        i += size
        matrices.append(matrix)
    return matrices



