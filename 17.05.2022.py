class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print("{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))


class Textile:
    def __init__(self, size, height):
        self.size = size
        self.height = height


    def one_coat(self):
        return self.size/6.5 + 0.5

    def one_suit(self):
        return self.height * 2 + 0.3

    @property

    def all_fabric(self):
        return str(f"Общий расход ткани: " + self.size/6.5 + 0.5 + self.height* 2 + 0.3)

class Coat(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.one_coat = round(self.size/6.5 + 0.5)

    def __str__(self):
        return f"Расход ткани на пальто: {self.one_coat}"


class Suit(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.one_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f"Расход ткани на пиджак: {self.one_suit}"


coat = Coat(1, 2)
suit = Suit(2, 3)
print(coat)
print(suit)