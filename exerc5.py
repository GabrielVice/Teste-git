preco = float(input("Digite o valor do produto R$: "))
descoto = preco - (preco*5/100)


print("O Valor do seu produto com 5% desconto fica R${:.2f} ".format(descoto))