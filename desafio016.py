# programa para mstrar só a parte inteira de um numero float


from math import trunc # comando para importar somente a função trunc da bilblioteca math

num=float(input('digite um numero com ponto decimal.'))
print('A parte inteira de {} é {}'.format(num,trunc(num)))
