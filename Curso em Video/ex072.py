lista = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoite','Dezenove','Vinte')

while True:
    Núm = int(input('Digite um número: '))
    while Núm > 20 or Núm < 0:
        Núm = int(input('Digite um número VÁLIDO! (Entre 0 e 20): '))
    print(f'O número digitado foi: {lista[Núm]}')
    continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break