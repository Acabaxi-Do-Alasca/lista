d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
y = int(input("Digite o ano: "))
bissexto = False
vntv = False
vnto = True

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    bissexto = True

if m == 2 and bissexto == True:
    vntv = True
    vnto = False

if m == 2 and bissexto == False and vntv == False or m > 12 and d > 31 and m != 2 or d < 0 or m < 0 or y < 0: 
    print(str(d)+"/"+str(m)+"/"+str(y),"A data não e valida")
elif m == 2 and bissexto == True and vntv == True or m <= 12 and d <= 31 and m != 2 or m == 2 and vnto == True and d <= 28:
    print(str(d)+"/"+str(m)+"/"+str(y),"A data e valida")