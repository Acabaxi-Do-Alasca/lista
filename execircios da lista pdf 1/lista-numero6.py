import os 
slm = float(input("Informe seu salario minino sem $: "))
vapqw = float(input("Informe o quanto você deve pagar sem $: "))
slmf = (slm / 7) / 100
valpqf = vapqw * slmf
des = valpqf * 0.1
valorTotal = valpqf - des
print("Valor do quilowatt:",str(slmf),"$","\nValoor a ser pago: ",str(valpqf),"$","\nvalor a ser pago com desconto: ",str(valorTotal),"$")
os.system("pause")