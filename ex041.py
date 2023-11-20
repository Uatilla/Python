from datetime import datetime
now = datetime.now()
yr = int(now.year)
id = int(input('Digite o seu ano de nascimento: '))
n = yr - id
if n <= 9:
    print('Com base na sua idade de {} anos, você é da classe MIRIM.'.format(n))
elif n <= 14:
    print('Com base na sua idade de {} anos, você é da classe INFANTIL.'.format(n))
elif n <= 19:
    print('Com base na sua idade de {} anos, você é da classe JUNIOR.'.format(n))
elif n <= 20:
    print('Com base na sua idade de {} anos, você é da classe SÊNIOR.'.format(n))
else:
    print('Com base na sua idade de {} anos, você é da classe MASTER.'.format(n))