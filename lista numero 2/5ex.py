n1 = int(input("Coloque o primeiro numero: "))
n2 = int(input("Coloque o segundo numero: "))

if n1 == 0 or n2 == 0 :
    print("Impossivel dividir por 0")
else:
    if n1 % n2 == 0:
        print(str(n1),"E divisivel por",str(n2))
    else:
        print(str(n1),"Não e divisivel por",str(n2))