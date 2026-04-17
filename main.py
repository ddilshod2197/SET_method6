# COPY
class MySet:
    def __init__(self):
        self.data = []

    def copy(self):
        yangi = []
        for item in self.data:
            yangi.append(item)
        return yangi

    def show(self):
        print(self.data)

s = MySet()
s.data = [5, 10, 15]

nusxa = s.copy()

print(nusxa)   

nusxa.append(20)
print(nusxa) 
s.show()       
