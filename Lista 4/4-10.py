a = int(input())
s = 0
for x in range(1, a+1):
    s = s+(x/(x*x))
print(f"S={s:.2f}")