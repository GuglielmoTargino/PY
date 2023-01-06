#programa para calcular a hipotenusa de um triangulo retangulo
from math import hypot
y=float(input('digite o valor do cateto oposto.'))
x=float(input('digite o valor do cateto adjacente.'))
#h=sqrt((pow(x,2)+pow(y,2)))
h=hypot(y,x)
print('A hipotenusa é {:.2f}'.format(h))

