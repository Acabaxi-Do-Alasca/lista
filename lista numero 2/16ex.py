n = int(input("Quantos lado do poligno regular: "))
m = int(input("Qual a medida do lado: "))

if n == 3:
    p = m + m + m
    print("TRIANGULO perímetro=",str(p))
elif n < 3:
    print("Não e um poligno")
elif n == 4:
    a = m * m
    print("QUADRADO area=",str(a))
elif n == 5:
    print("PENTAGONO")
else:
    print("Poligno não identificado")