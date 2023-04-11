import os 
r = float(input("Qual o raio da lata de oleo: "))
pi = 3.1416
h = float(input("Qual a altura da lata de oleo: "))
v = pi * (r*r) * h

print("O volume da lata e de: ",str(v))
os.system("pause")