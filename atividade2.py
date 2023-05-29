lista = []


for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    lista.append(valor)


print("Maior valor da lista:", max(lista))


print("Menor valor da lista:", min(lista))


print("Média dos valores da lista maior e menor:", max(lista) / min(lista))