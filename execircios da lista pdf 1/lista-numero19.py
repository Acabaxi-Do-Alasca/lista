import os 
nm = input("Informe o numero da conta: ")

smi = int(nm[2] + nm[1] + nm[0])
soma = smi + int(nm)
soma = str(soma)


mt = int(soma[0])*1 + int(soma[1])*2 + int(soma[2])*3

print ("o digito verificador e: ",str(mt)[1])
os.system("pause")