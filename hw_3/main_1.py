import numpy as np
from matrix_1 import Matrix


def main():
    np.random.seed(0)

    matrix1_data = np.random.randint(0, 10, (10, 10))
    matrix2_data = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    result_add = matrix1 + matrix2
    result_mul = matrix1 * matrix2
    result_matmul = matrix1 @ matrix2

    with open("artefacts/1_matrix+.txt", "w", encoding="utf-8") as f:
        f.write(str(result_add))

    with open("artefacts/1_matrix*.txt", "w", encoding="utf-8") as f:
        f.write(str(result_mul))

    with open("artefacts/1_matrix@.txt", "w", encoding="utf-8") as f:
        f.write(str(result_matmul))


if __name__ == "__main__":
    main()
