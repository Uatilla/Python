frase = str(input('Digite uma frase: ')).lower()
string = frase[::-1]
fr1=frase.replace(' ','')
fr2=string.replace(' ','')
if fr1 == fr2:
    print('A frase que você digitou é um PALÍNDROMO')
else:
    print('A frase que você digitou não é um PALÍNDROMO')