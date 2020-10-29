import math as m

#Complex number class
class Complex:
    def __init__(self, real, imag):
        self.a = real
        self.b = imag

    def conv(self):
        return Polar(m.sqrt(self.a**2 + self.b**2), m.atan(self.b/self.a)*180)

    def print(self):
        if self.b >= 0: sign = "+"
        else: sign = "-"
        print(str(self.a) + sign + str(abs(self.b)) + 'j', end = '')

#Complex number in polar form class
class Polar:
    def __init__(self, val, angle):
        self.val = val
        self.angle = angle

    def conv(self):
        return Complex(self.val*m.cos(self.angle), self.val*m.sin(self.angle))

    def print(self):
        self.conv().print()

    def printPolar(self):
        print(str(truncate(self.val,2)) + '|_' + str(truncate(self.angle,2)) + '°', end = '')

#Truncate function (found on StackOverflow, written by David Z)
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

#Divide a complex number in polar form
def divPol (p1, p2):
    return Polar(p1.val/p2.val, p1.angle-p2.angle)

#Product of two complex numbers (FOIL)
def cProd (c1, c2):
    a = (c1.a * c2.a) + (-1)*(c1.b * c2.b)
    b = (c1.a * c2.b) + (c1.b * c2.a)
    return Complex(a, b)

#Sum of complex numbers
def cSum (c1, c2):
    return Complex(c1.a+c2.a, c1.b+c2.b)

#Difference of complex numbers
def cDif (c1, c2):
    return Complex(c1.a-c2.a, c1.b-c2.b)

#Product of a complex and a real number
def crProd (c, r):
    return Complex(c.a*r, c.b*r)


#Find the determinant of a 2d array
def subDet (arr):
    c1 = cProd(arr[0][0], arr[1][1])
    c2 = cProd(arr[0][1], arr[1][0])
    return cDif(c1, c2)

#Find the determinant of the given array
def findDet (arr):
    det = Complex(0,0)
    sign = True
    for top in range(len(arr[0])):
        subA = subArr(arr, top)
        prod1 = cProd(subA[0][0], subA[1][1])
        prod2 = cProd(subA[0][1], subA[1][0])
        prodDif = cDif(prod1, prod2)
        detProd = cProd(arr[0][top], prodDif)
        if sign:
            det = cSum(det, detProd)
            sign = False
        else:
            det = cDif(det, detProd)
            sign = True
    return det

#
def subArr(arr, exclude):
    subArr = []
    for i in range(len(arr)-1):
        subArr.append([])
    i = 0
    j = 0
    for x in range(len(arr[0])):
        for y in range(1, len(arr)):
            if x != exclude:
                subArr[i].append(arr[y][x])
                i += 1
                if y == len(arr)-1:
                    i = 0
                    j += 1
    return subArr

#Return the DeterminantX array, to be divided by the determinant array
def detArr(arr1, arr2, col):
    newArr = []
    k = 0
    for i in range(len(arr1)):
        newArr.append([])
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if j == col:
                newArr[i].append(arr2[k])
                k += 1
            else:
                newArr[i].append(arr1[i][j])
    return newArr

#Print integers or complex numbers
def choosePrint(el):
    if type(el) == int:
        print(str(el), end = '')
    else:
        el.print()

#Format and print the contents of the array
def printArr(arr):
    for i in arr:
        print("[\t", end = '')
        if type(i) == list:
            for j in i:
                choosePrint(j)
                print(",\t", end = '')
            print("]")
        else:
            choosePrint(i)
            print(" ]")

imped = [   [ Complex(1,2), Complex(0,-2), Complex(-1,0) ],
            [ Complex(0,-2), Complex(2,-1), Complex(0,3) ],
            [ Complex(-1,0), Complex(0,3), Complex(1,-3) ]  ]
volts = [ Polar(3, 0).conv(), Polar(0,0).conv(), Polar(6, 0).conv() ]
sep = "-----------------------------------------"


printArr(imped)
printArr(volts)
print('\n\n')

#Determinant
det = findDet(imped)
detPol = det.conv()
#Determinant A
detArrA = detArr(imped, volts, 0)
detA = findDet(detArrA)
detAPol = detA.conv()
i1 = divPol(detAPol, detPol)
#Determinant B
detArrB = detArr(imped, volts, 1)
detB = findDet(detArrB)
detBPol = detB.conv()
i2 = divPol(detBPol, detPol)
#Determinant C
detArrC = detArr(imped, volts, 2)
detC = findDet(detArrC)
detCPol = detC.conv()
i3 = divPol(detCPol, detPol)
#print arrays and results (Verbose)
printArr(detArrA)
print(sep)
printArr(imped)
print(" = ", end = '')
detA.print()
print(" / ", end = '')
det.print()
print(" = ", end = '')
detAPol.printPolar()
print(" / ", end = '')
detPol.printPolar()
print(" = ", end = '')
i1.printPolar()
print('\n')

printArr(detArrB)
print(sep)
printArr(imped)
print(" = ", end = '')
detB.print()
print(" / ", end = '')
det.print()
print(" = ", end = '')
detBPol.printPolar()
print(" / ", end = '')
detPol.printPolar()
print(" = ", end = '')
i2.printPolar()
print('\n')

printArr(detArrC)
print(sep)
printArr(imped)
print(" = ", end = '')
detC.print()
print(" / ", end = '')
det.print()
print(" = ", end = '')
detCPol.printPolar()
print(" / ", end = '')
detPol.printPolar()
print(" = ", end = '')
i3.printPolar()
print()
