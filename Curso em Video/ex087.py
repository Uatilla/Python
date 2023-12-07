mtx = [[],[],[]]
par = tcol = 0
for l in range(0,3):
    for c in range(0,3):
        mtx[l].append(int(input(f'Digite um valor na posição [{l}, {c}]: ')))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mtx[l][c]:^5}]',end='')
    print()
print('-='*30)
for gl in mtx:
    for el in gl:
        if el %2 == 0:
            par += el
    tcol += gl[2]
print(f'A soma total dos pares é {par}.')
print(f'A soma da terceira coluna é {tcol}.')
print(f'O maior valor da segunda linha é {max(mtx[1])}.')



