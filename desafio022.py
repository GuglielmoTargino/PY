

nome=str(input('digete um nome_')).strip()# strp retira os espaços do começo e do fim da string


print(' o nome em maousculo é {}'.format(nome.upper())) #maiuscula
print('o nome em minusculo é {}'.format(nome.lower())) #minusculo
print('a qtd de letras do nome é {}'.format(len(nome)-nome.count(' ')))
print(' o primeiro nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()# split coloca o nome em ordem de lista iniciando na posi 0.
print(' o primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

