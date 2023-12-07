def write(line):
    tam = int(len(line)+2)
    print('~'* tam)
    print(f'{line:^{tam}}')
    print('~' * tam)


# main program
f0 = str(input('DIGITE A PRIMEIRA FRASE: '))
f1 = str(input('DIGITE A SEGUNDA FRASE: '))
f2 = str(input('DIGITE A TERCEIRA FRASE: '))
write(f0)
write(f1)
write(f2)