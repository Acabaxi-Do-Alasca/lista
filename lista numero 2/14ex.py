c = int(input("Qual o numero do aluno: "))
n1 = int(input("Qual a primeira nota: "))
n2 = int(input("Qual a segunda nota: "))
n3 = int(input("Qual a terceira nota: "))
me = int(input("Qual a media de exercicios feitos: "))
ma = (n1 + (n2*2) + (n3*3) + me)/7

if ma >= 9:
    co = "A"
elif ma >= 7.5 and ma < 9:
    co = "B"
elif ma >= 6 and ma < 7.5:
    co = "C"
elif ma >= 4 and ma < 6:
    co = "D"
else:
    co = "E"

if co == "A" or co == "B" or co == "C":
    print("O aluno",str(c),"foi APROVADO com o conceito",co,"MA=",str(ma))
else:
    print("O aluno",str(c),"foi REPROVADO com o conceito",co,"MA=",str(ma))