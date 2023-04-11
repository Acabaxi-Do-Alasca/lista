import os
import math 
pc = float(input("Informe o primeiro cateto: "))
sc = float(input("Informe o segundo cateto: "))
h = ((pc*pc) + (sc*sc))
h = math.sqrt(h)

print("A hipotenusa e de ",h)
os.system("pause")