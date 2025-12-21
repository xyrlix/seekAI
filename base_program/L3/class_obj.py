class MyClass:
    """ A simple example class """
    i = 12345
    def f(self):
        return 'hello world' + str(self.i)

print(MyClass.i)
print(MyClass.f)
# print(MyClass.f())
x = MyClass()
print(f'{x} : {x.i} : {x.f()}')



class Warehouse:
    # class variable
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(f'{w1} : {w1.purpose} : {w1.region}')
w2 = Warehouse()
w2.region = 'east' # instance variable
print(f'{w2} : {w2.purpose} : {w2.region}')
print(Warehouse.__dict__)
Warehouse.newClassVar = 'new'
print(Warehouse.__dict__)
print(w1.__dict__)
print(w2.__dict__)