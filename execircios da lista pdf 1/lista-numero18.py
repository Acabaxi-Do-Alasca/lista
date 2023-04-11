import os 
qnt = int(input("Digite a quantidade de fitas que possui: "))
vla = int(input("Qual o valor que cobra por cada aluguel: "))
qntm = qnt / 3
vl = qntm * vla
qnta = qntm * 12
valor = qnta * vla
qntdatr = (vl / 10) * 0.1
qntf2 = qnt * 0.02
qntf10 = ((qnt / 10) + qnt) - qntf2

print("Faturamento anual: ",str(valor),"\nValor de multas mensais: ",str(qntdatr),"\ntotal de fitas no final de um ano: ",qntf10)
os.system("pause")