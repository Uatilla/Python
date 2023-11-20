from datetime import datetime
now = datetime.now()
yr = int(now.year)
s=0
for c in range(0,7):
    n = int(input('Digite o ano de nascimento: '))
    if (yr-n)>=21:
        s = s + 1
print('{} pessoas são maiores de idade'.format(s))
print('{} pessoas ainda não atingiram a maior idade'.format(7-s))