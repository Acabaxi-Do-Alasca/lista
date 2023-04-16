i = int(input("Qual a tua idade: "))

if i <= 12 :
    print("Criança")
elif i >= 13 and i <= 19:
    print("Adolescente")
elif i >= 20 and i<= 50:
    print("Adulto")
else :
    print("Idoso")