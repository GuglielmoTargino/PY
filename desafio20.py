#programa feito para selecionar aleatoriamente uma ordem de exibição

import random
nm1=str(input('digite o primweiro nome'))
nm2=str(input('digite o segundo nome'))
nm3=str(input('digite o terceiro nome'))
nm4=str(input('digite o quarto nome'))
lista=[nm1,nm2,nm3,nm4]
random.shuffle(lista) # shuffle serve para embaralhar
print(lista)