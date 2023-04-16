i = int(input("Qual a tua idade: "))
a = int(input("Quantos anos de trabalho: "))

if i >= 65 or a >= 30 or i >= 60 and a >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")