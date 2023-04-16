sb = int(input("Fale teu salario bruto: "))
pr = int(input("Fale teu provento: "))

if sb <= 5000 :
    des = sb * 0.05
    sl = sb + pr - des
    print("Seu salário líquido é de R$ {:.2f}".format(sl))
else :
    des = sb * 0.1
    sl = sb + pr - des
    print("Seu salário líquido é de R$ {:.2f}".format(sl))