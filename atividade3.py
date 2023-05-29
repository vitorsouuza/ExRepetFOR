pessoas = int(input("Digite a quantidade de pessoas a serem analisadas: "))
temperaturas = 0

for i in range(pessoas):
    temp = float(input(f"temperatura da pessoa {i+1}: "))
    temperaturas += temp
    if temp < 37.2:
        print("Temperatura normal")
    elif 37.3 <= temp <= 38.0:
        print("Estado febril")
    elif 38.1 <= temp <= 39.0:
        print("Com febre")
    else:
        print("Com febre alta")

temperaturas = temperaturas / pessoas
print("a media é ", temperaturas)


