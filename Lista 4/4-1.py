começo = True
xme = 0
xma = 0
while começo == True:
    x = int(input())
    if x < xme:
        xme = x
    if x < 0:
        começo = False
    if x > xma:
        xma = x
    if xma == 0:
        xma = xme
print(f"Menor: {str(xme)} Maior: {str(xma)}")