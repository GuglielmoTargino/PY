# programa para fazer um sorteio 
import random

#nome1=input('digite o primeiro nome')
#nome2=input('digite o segundo nome')
#nome3=input('digite o terceiro nome')
#nome4=input('digite o quarto nome')
#print(' nomes são 1º{}, 2º{}, 3º{}, 4º{}'.format(nome1, nome2, nome3, nome4))

#sel=random.randint(1,4)
#print('o escolhido foi {}º'.format(sel))


n1=str(input('digite o primeiro nome'))
n2=str(input('digite o segundo nome'))
n3=str(input('digite o terceiro nome'))
n4=str(input('digite o quarto nome'))
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print('o nome escolhido foi:{}'.format(escolhido))

