mtx = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        mtx[l].append(int(input(f'Digite um valor na posição [{l}, {c}]: ')))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mtx[l][c]:^5}]',end='')
    print()