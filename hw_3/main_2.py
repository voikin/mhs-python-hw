import numpy as np
from matrix_2 import Matrix


def main():
    np.random.seed(0)

    matrix1_data = np.random.randint(0, 10, (10, 10))
    matrix2_data = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    result_add = matrix1 + matrix2
    result_mul = matrix1 * matrix2
    result_matmul = matrix1 @ matrix2

    matrix1.save_to_file("artefacts/matrix_1_serialized.json", format="json")
    matrix2.save_to_file("artefacts/matrix_2_serialized.pkl", format="pickle")

    with open("artefacts/2_matrix+.txt", "w", encoding="utf-8") as f:
        f.write(str(result_add))
    with open("artefacts/2_matrix*.txt", "w", encoding="utf-8") as f:
        f.write(str(result_mul))
    with open("artefacts/2_matrix@.txt", "w", encoding="utf-8") as f:
        f.write(str(result_matmul))


if __name__ == "__main__":
    main()
