from sympy import *
from sympy.abc import x,y

print("\nProgram menghitung integral dengan menggunakan metode Simpson \n")
print("Baca https://en.wikibooks.org/wiki/Python_Programming/Basic_Math untuk operasi matematika dasar di bahasa Python \n")
print("---------------------------------------------------------------------------------------------------------------- \n")

func = simplify(input("Masukkan fungsi : "))
a = float(input("Masukkan batas atas : "))
b = float(input("Masukkan batas bawah : "))
print("\n!!! NOTE !!! \nmasukkan untuk tiap n ketelitian yang diinginkan. semakin besar n, semakin teliti angka yang dihasilkan di belakang koma\n")
n = int(input("Masukkan n (harus genap) : "))

delta=(b-a)/n
total = 0

for z in range(n+1) :
    y = func.subs(x,(a+z*delta))

    if(z%2 == 0 and (z != n and z != 0)) :
        y = y*2
    elif(z%2 == 1 and (z != n and z != 0)) :
        y = y*4
        
    total = total+y

result = delta*total/3
print("\nHasil : " + str(result) + "\n")
