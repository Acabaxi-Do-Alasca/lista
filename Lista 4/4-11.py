x=0
alunos=0
lpmf=0
gosta=0
fim=1
while fim==1:
    s=int(input())
    if s==0:
        fim=0
    else:
        lpm=int(input())
        r=int(input())
        x=x+1
        if s==3:
            alunos=alunos+1
            if r==0:
                gosta=gosta+1
        if s==4:
            if lpm>lpmf:
                lpmf=lpm
print(f"ALUNOS 3a SERIE:{int(alunos)}\nMAIOR QTD LIVROS 4a SERIE:{int(lpmf)}")
if alunos==0:
    print("IMPOSSIVEL CALCULAR % NENHUM ALUNO NA 3a SERIE!")
else:
    print(f"NAO GOSTAM REDACAO 3a SERIE:{int(gosta/alunos*100)}%")