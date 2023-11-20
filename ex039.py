from datetime import datetime
now = datetime.now()
yr = int(now.year)
id = int(input('Digite o seu ano de nascimento: '))
n = yr - id
if n == 18:
    print('Como estamos no ano de {} e você tem {} anos de idade, logo, deve se apresentar na junta militar este ano.'.format(yr,n))
elif n > 18:
    d = n-18
    print('Como estamos no ano de {} e você tem {} anos de idade, logo, você deveria ter se apresentado na junta militar há {} anos atrás.'.format(yr,n,d))
else:
    d = 18-n
    print(
        'Como estamos no ano de {} e você tem {} anos de idade, logo, você deverá se apresentar na junta militar daqui há {} anos.'.format(yr, n, d))