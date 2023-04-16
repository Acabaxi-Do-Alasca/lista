i = int(input("Qual a idade do nadador: "))

if i <= 4:
    print("Idade não valida")
elif i >= 5 and i <= 7:
    print("Infantil A")
elif i >= 8 and i <= 10:
    print("Infantil B")
elif i >= 11 and i <= 13:
    print("Juvenil A")
elif i >= 14 and i <= 17:
    print("Juvenil B")
else:
    print("Sênior")