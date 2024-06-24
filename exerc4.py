altura = float(input(" Diga qual a altura da parede em metros: "))
largura = float(input("Diga a largura da parede em metros:  "))

metro = altura*largura
litro = metro/2

print("Sua parete tem {}m² e precisa de {:.1f}Lts de tinta para pintura".format(metro,litro))

