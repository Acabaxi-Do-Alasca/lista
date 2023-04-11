import os 
A = input("Faler qualquer coisa: ")
B = input("Fale novamente qualquer coisa: ")
print("Apos a leitura A=",str(A),"B=",str(B))
A,B = B,A
print("Apos a troca A=",str(A),"B=",str(B))
os.system("pause")