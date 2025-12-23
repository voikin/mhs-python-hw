class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(self.data)
        self.cols = len(self.data[0]) if self.rows > 0 else 0

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Несовместимые размерности для сложения: "
                f"({self.rows}, {self.cols}) и ({other.rows}, {other.cols})"
            )

        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]

        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Несовместимые размерности для покомпонентного умножения: "
                f"({self.rows}, {self.cols}) и ({other.rows}, {other.cols})"
            )

        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]

        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                f"Несовместимые размерности для матричного умножения: "
                f"({self.rows}, {self.cols}) @ ({other.rows}, {other.cols})"
            )

        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]

        return Matrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])
