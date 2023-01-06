# fazer um programa que separe um numero em unida,dezena,centena e milhar.
num=int(input('digite um numero_'))
u=num//1%10 # O // pega o resultado inteiro da divisão. Já o % pega o que vem depois da virgula _-
            #_- (o resto da divisão) no caso, o digito de sobrou da divisão por 10. 
d=num//10%10
c=num//100%10
m=num//1000%10
print('o numero {} tem {} unidades'.format(num,u))
print('o numero {} tem {} dezenas'.format(num,d))
print('o numero {} tem {} centenas'.format(num,c))
print('o numero {} tem {} milhar'.format(num,m))