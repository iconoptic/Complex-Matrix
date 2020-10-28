class Complex:
    def __init__(self, real, imag):
        self.a = real
        self.b = imag 

    def print(self):
        if self.b >= 0: sign = "+" 
        else: sign = "-"
        print(str(self.a) + sign + str(abs(self.b)) + 'j', end = '')

def cProd (c1, c2):
    a = (c1.a * c2.a) + (-1)*(c1.b * c2.b)
    b = (c1.a * c2.b) + (c1.b * c2.a)
    return Complex(a, b)

def crProd (c, r):
    return Complex(c.a*r, c.b*r)

def printArr(arr):
    for i in arr:
        print("[\t", end = '') 
        if type(i) == list:
            for j in i:
                if type(j) == int:
                    print(j, end = '') 
                else:
                    j.print()
                print(",\t", end = '') 
            print("]")
        else:
            print(str(i) + " ]")

terms = [[-10, Complex(2, 4)], [Complex(3,-1), -10]]
ans = [20, 40]
printArr(terms)
printArr(ans) 
