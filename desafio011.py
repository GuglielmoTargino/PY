#fazer um programa que calcule a área de uma parede >>
# e quanta tinta vai gastar para pintá-la com uma tinta >>
# que pinta 2m2 com um litro.
  
alt=float(input('informe a altura da parede em metros.'))
lar=float(input('informe a largura da parede em metros'))
a=alt*lar

tg=a/2

print('a área da parede é {} metros. E gastará {} litros de tinta'.format(a,tg))