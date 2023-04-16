c = int(input("Qual o código do aluno: "))
n1 = int(input("Qual a primeira nota: "))
n2 = int(input("Qual a segunda nota: "))
n3 = int(input("Qual a terceira nota: "))
aprovado = False

if n1 > n2 and n1 > n3:
    m = ((n1*4)+(n2*3)+(n3*3))/10
elif n2 > n1 and n2 > n3:
    m = ((n2*4)+(n1*3)+(n3*3))/10
else:
    m = ((n3*4)+(n1*3)+(n2*3))/10

if m > 5:
    aprovado = True

if aprovado == True:
    print("código=",str(c),"Nota1=",str(n1),"Nota2=",str(n2),"Nota3=",str(n3),"Media =",str(m),"APROVADO")
else:
    print("código=",str(c),"Nota1=",str(n1),"Nota2=",str(n2),"Nota3=",str(n3),"Media =",str(m),"REPROVADO")