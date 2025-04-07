h1 = int(input("digite a hora 1:"))
m1 = int(input("digite o minuto 1:"))
h2 = int(input("digite a hora 2:"))
m2 = int(input("digite o minuto 2:"))

if h1 >  12:
    h1 = h1 - 12
if h2 > 12:
    h2 = h2 - 12
somah = h1 + h2
if somah > 12:
    somah=somah - 12

somaM = m1 + m2



