# Создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число).
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.

class Cell:
    def __init__(self, partitions):
        self.partitions = partitions

    def __str__(self):
        return f'Количество ячеек в клетке: {self.partitions}.'

    def __add__(self, other):
        return Cell(self.partitions + other.partitions)

    def __sub__(self, other):
        if self.partitions > other.partitions:
            return Cell(self.partitions - other.partitions)
        else:
            return f'Нельзя вычесть больщую клетку из меньшей'

    def __mul__(self, other):
        return Cell(self.partitions * other.partitions)

    def __truediv__(self, other):
        return Cell(self.partitions // other.partitions)

    def make_order(self, elements):
        return "\n".join([";) " * elements for _ in range(self.partitions // elements)]) \
               + "\n" + ("(: " * (self.partitions % elements))


cell_1 = Cell(12)
cell_2 = Cell(7)

print(cell_1)
print(cell_2)
print()
print(f'Сумма: {cell_1 + cell_2}')
print(f'Разность: {cell_1 - cell_2}')
print(f'Разность наоборот: {cell_2 - cell_1}')
print(f'Произведение: {cell_1 * cell_1}')
print(f'Частное: {cell_1 / cell_2}')
print()
print(cell_1.make_order(3))
print(cell_2.make_order(3))
