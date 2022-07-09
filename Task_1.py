# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join("\t".join([f"{el:3}" for el in row]) for row in self.matrix)

    def __add__(self, other):
        try:
            new_matrix = [[int(self.matrix[row][el]) + int(other.matrix[row][el])
                           for el in range(len(self.matrix[row]))]
                          for row in range(len(self.matrix))]
            return Matrix(new_matrix)
        except IndexError:
            return f"Можно сложить только матрицы одинакового размера"


matrix_1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matrix_2 = Matrix([[3, 3, 3], [-2, 2, 2], [-1, 1, 1]])
matrix_3 = Matrix([[10, 20], [30, 40]])

matrix_4 = matrix_1 + matrix_2
matrix_5 = matrix_1 + matrix_3

print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_4)
print()
print(matrix_5)
