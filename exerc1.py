n1 = float(input('Diginte um numero '))
n2 = float(input('Digite seu segundo numero '))
media  = (n1+n2)/2
m = float(input('Diga o numero de metros oara conversão '))
cent = m*100
mili = m*1000


print('o antecessor do seu numero é {} e o sucessor é {}'.format(n1-1,n1+1)  )
print('O dobro do seu numero é {} o triplo é {} e a raiz quadrada fica {}'.format( n1*2,n1*3,n1**(1/2)))

print('A media do aluno foi {:.1f}'.format(media))
print('A conversão de {}metros em centimetros é {} e em milimetros é {}'.format(m,cent,mili))



