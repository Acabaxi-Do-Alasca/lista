j = 1.50
a = 1.10
x = 0
while j > a:
    print(f"Apricocildo={a:.2f}m, Josberanilson={j:.2f}m")
    j = j + 0.02
    a = a + 0.03
    x = x + 1
print(f"Apricocildo={a:.2f}m, Josberanilson={j:.2f}m anos={str(x)}")