nome = str(input("Digite seu nome completo: ")).strip().title()
lista = nome.split()
print("Seu primeiro nome é {}".format(lista[0]))
print("Seu último nome é {}".format(lista[len(lista) - 1]))