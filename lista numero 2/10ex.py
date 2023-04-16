y = int(input("Digite o ano: "))

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("O ano",str(y),"e bissexto")
else:
    print("O ano",str(y),"não e bissexto")