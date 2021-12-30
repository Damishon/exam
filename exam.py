class Figure ():
    def __init__(self,myfunc ):
        self.myfunc = myfunc

    def area(self):
        pass

    def fact(self):
        return "двухмерная фигура"

    def __str__(self):
        return self.name


class Square(Figure):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "У квадратов каждый угол равен 90 градусам."


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
