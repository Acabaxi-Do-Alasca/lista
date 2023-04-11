import os 
des = int(input("Qual o valor do desconto: "))
des1 = des * 0.01
val = float(input("Qual o valor do produto: "))
valf = val * des1
valf2 = val - valf

print("Valor com desconto de ",str(des),"por cento: R$",str(valf2))
os.system("pause")