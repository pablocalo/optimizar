import array

class Optimizar:

    array=[]

    def inp(self):
        print("Introduzca un numero: ")
        return int(input())

    def add(self, n):
        self.array.append(n)

    def media(self):
        suma = 0
        for i in self.array:
            suma = suma + i
        if suma == 0:
            return 1
        else:
            return suma/len(self.array)

