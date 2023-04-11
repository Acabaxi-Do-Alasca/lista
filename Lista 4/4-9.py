bra = 0
nul = 0
kik = 0
cha = 0
chi = 0
ativo=True
while ativo==True:
    voto = int(input())
    if voto == 1:
        bra = bra + 1
    elif voto == 2:
        nul = nul + 1
    elif voto == 3:
        kik = kik + 1
    elif voto == 4:
        cha = cha + 1
    elif voto == 5:
        chi = chi + 1
    elif voto == 666:
        ativo = False
    else:
        break
if ativo == False:
    print(f"branco={str(bra)} nulo={str(nul)} kiko={str(kik)} chaves={str(cha)} chiquinha={str(chi)}")