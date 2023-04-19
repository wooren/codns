def multi (n):
    for r in range(2,6,1):
        print(f'{r}x{n}={n*r:2d}',end=" ")
    print()

def multi (n):
    for r in range(6,10,1):
        print(f'{r}x{n}={n*r:2d}',end=" ")
    print()

for x in range(1,10,1):
    multi(x)
print()
for y in range(1,10,1):
    multi(y)
      



