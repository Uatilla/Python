frase = str(input('Digite uma frase: ')).strip()
letra = str(input('Qual letra deseja analisar: '))
frasel = frase.lower()
print('Na frase {} existem {} letras {}.'.format(frase, frasel.count(letra),letra))
print('A primeira letra {}, encontra-se na posição {}.'.format(letra, frasel.find(letra)+1))
print('A última letra {}, encontra-se na posição {}.'.format(letra, frasel.rfind(letra)+1))