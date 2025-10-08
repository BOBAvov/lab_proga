mass = list(map(int,input().split()))
idx_0 = None
idx_max = mass[0]
for i,v in enumerate(mass):
    if v == 0:
        idx_0 = i
    if v > mass[idx_max]:
        idx_max = i
if idx_0 is None:
    print('В ведённом списке нет 0')
else:
    mass[idx_0],mass[idx_max] =  mass[idx_max], mass[idx_0]
    print(mass)