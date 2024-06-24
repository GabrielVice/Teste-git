"""
python operadores

** potenciação
// divição inteira
% resto da divição

"""

nome = input('Qual o seu nome? ')
n1 = int(input('primeiro numero '))
n2 = int(input('segundo numero '  ))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é {} o produto é {} e a divisão é {:.3f}'.format(s,m,d))
print("divisão inteira fica {} e a potencia fica {}".format(di,e))
print('O resultado da sua conta foi {}'.format(di))
print(' A soma dos seus numeros é {}'.format(n1+n2))
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer novamente {:>20}!!'.format(nome))
print('Prazer novamente {:<20}!!'.format(nome))
print('Prazer novamente {:^20}!!'.format(nome))
print('Prazer novamente {:=>20}!!'.format(nome))
print('Prazer novamente {:=^20}!!'.format(nome))

