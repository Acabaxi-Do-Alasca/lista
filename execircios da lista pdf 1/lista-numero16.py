import os 
v = int(input("Qual o valor: "))
tx = float(input("Qual a taxa: "))
tm = int(input("Qual o tempo: "))

p = v + (v * (tx/100) * tm)
print("a prestação e: ",p)
os.system("pause")