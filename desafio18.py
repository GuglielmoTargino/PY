#programa para calcular seno, cosseno e tangente de um angulo
import math
num=int(input('digite um angulo'))
s=math.sin(math.radians(num))
c=math.cos(num) # falta converter para radiano
t=math.tanh(num)# falta converter para radiano
print('o seno de {} é {}, cosseno é {}, tangente é {}'.format(num,s,c,t))
