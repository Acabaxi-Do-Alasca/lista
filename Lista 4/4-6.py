inferior = int(input())
superior = int(input())
decremento = int(input())
r = -1
for x in range(superior, inferior+1, -decremento):
    r = r + 1
    c = superior-decremento*r
    f = (c*9/5)+32
    print(str(c)+"C="+str(f)+"F")