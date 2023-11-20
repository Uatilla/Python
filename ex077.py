tupla = ('aprender','programar','linguagem','python')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos ',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra,end='')

