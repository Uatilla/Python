núm = []
for n in range (0,5):
    núm.append(int(input('Digite um número: ')))
print('-'*40)
print(f'\nA lista digitada foi {núm}.')
print(f'O maior valor é {max(núm)} e está nas posições ',end='')
for i, v in enumerate(núm):
    if v == max(núm):
        print(f'{i}...',end=' ')
print(f'\nO menor valor é {min(núm)} e está nas posições ',end='')
for i, v in enumerate(núm):
    if v == min(núm):
        print(f'{i}...',end=' ')
