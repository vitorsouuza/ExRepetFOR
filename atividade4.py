idademulheres = 0
qtdmulheres = 0
idadehomens = 0
qtdhomens = 0
media= 0



for i in range(0, 10):
    idade = int(input(f"qual é sua idade {i+1}: "))
    sexo = input(f"qual é seu sexo {i+1}: ")
    if sexo == 'masculino':
        qtdhomens += 1
        print('a quantidade de homens é : ', qtdhomens )
        idadehomens += idade
    elif sexo == 'feminino':
        qtdmulheres += 1
        idademulheres+= idade
        print('a quantidade de mulheres é: ', qtdmulheres)

calcF = idademulheres / qtdmulheres
print("a media das mulheres :",calcF)
calcH = idadehomens / qtdmulheres
print('a media dos homens :',calcH)

total = (idademulheres+idadehomens)/10
print('o total da media dos grupos e :',total)
print(' a quantidade de homens é',qtdhomens)
print(' a quantidade de mulheres é',qtdmulheres)

