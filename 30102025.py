
# Обычные задания

#1
get_kvadr= lambda m: m*m
print(get_kvadr(2))
print(get_kvadr(4))
print(get_kvadr(6))
print(get_kvadr(8))
print(get_kvadr(10))

#2
numbers = [2, 4, 6, 8, 10]
dev = list(map(lambda x: x/2, numbers))
print(dev)

#3
numbers_1= [10, 15, 20, 25, 30]
filt_numb = list(filter(lambda c: c<25, numbers_1))
print(filt_numb)



# Сложные задания 1-4 объединено в 1 код

class Shape:
    def area(self):
        pass

class Circle(Shape)    :
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
shapes = [Circle(4), Square(9), Circle(15), Square(78)]
areas = list(map(lambda shape: shape.area(), shapes))
large_shapes = list(filter(lambda shape: shape.area() > 20, shapes))
sorted_shapes = sorted(large_shapes, key=lambda shape: shape.area(), reverse=True)
print(areas)


for shape in sorted_shapes:
    print(f"{type(shape).__name__} с площадью {shape.area()}")
    
