"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input("Quantos dias foram alugados? "))
km = float(input("Quantos Km foram percorridos? "))


Total = (dias*60)+(km*0.15)

print("O valor do seu aluguel ficou R${:.2f}".format(Total))
