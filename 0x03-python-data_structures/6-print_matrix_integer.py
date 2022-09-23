def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        new_list = []
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("")
