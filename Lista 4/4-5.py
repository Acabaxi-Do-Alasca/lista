inferior = int(input())
superior = int(input())
incremento = int(input())
for x in range(inferior, superior+1, incremento):
    if superior < inferior:
        break
    elif incremento > superior:
        print(str(inferior))
    else:
        print(str(x))