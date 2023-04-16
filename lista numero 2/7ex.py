h = float(input("Digite sua altura: "))
s = input("Digite teu sexo M ou F: ")

if s == "m":
    s2 = (72.7 * h) - 58
    print("O teu peso ideal e de: ",s2)
elif s == "f":
    s2 = (62.1 * h) - 44.7
    print("O teu peso ideal e de: ",s2)