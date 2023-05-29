homem_novo = 0
homem_velho = 0
homens_mediano =0
idadeh = 21

for i in range(2):
    nomes = input(f"qual é seu nome: {i+1}: ")
    idade = int(input(f"qual é sua idade {i + 1}: "))
if idade > idadeh:
 homem_velho+= nomes, idade

elif idade<=20:
       homem_novo+= 1
       print('a quantidade de homens mais novos são :', homem_novo)


print('o homens mais velho é :', homem_velho)




