from matrix_3 import Matrix
from matrix_1 import Matrix as BaseMatrix


def get_collision_matrices():
    A = Matrix([[1, 2], [3, 4]])
    C = Matrix([[2, 1], [4, 3]])

    assert hash(A) == hash(C), "A и C должны иметь одинаковый хеш"
    assert A != C, "A и C должны быть разными"

    B = Matrix([[0, 1], [1, 0]])
    D = Matrix([[0, 1], [1, 0]])

    AB = Matrix(BaseMatrix.__matmul__(A, B).data)
    CD = Matrix(BaseMatrix.__matmul__(C, D).data)

    assert AB != CD, "A @ B должен быть не равен C @ D"

    return A, B, C, D


def main():
    A, B, C, D = get_collision_matrices()

    AB = A @ B
    CD = Matrix(BaseMatrix.__matmul__(C, D).data)

    with open("artefacts/A.txt", "w", encoding="utf-8") as f:
        f.write(str(A))

    with open("artefacts/B.txt", "w", encoding="utf-8") as f:
        f.write(str(B))

    with open("artefacts/C.txt", "w", encoding="utf-8") as f:
        f.write(str(C))

    with open("artefacts/D.txt", "w", encoding="utf-8") as f:
        f.write(str(D))

    with open("artefacts/AB.txt", "w", encoding="utf-8") as f:
        f.write(str(AB))

    with open("artefacts/CD.txt", "w", encoding="utf-8") as f:
        f.write(str(CD))

    with open("artefacts/hash.txt", "w", encoding="utf-8") as f:
        f.write(f"hash(AB) = {hash(AB)}\n")
        f.write(f"hash(CD) = {hash(CD)}\n")


if __name__ == "__main__":
    main()
