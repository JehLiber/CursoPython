# Exercício IMC - Peso de Massa Corporal 
# Calcula o IMC de acordo com o peso e altura informados
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc =  peso / (altura * altura)  #  calculo do IMC = peso / (altura * altura)


#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura' #altura:.2f é para colocar casa decimais 
linha_2 = f'pesa {peso} quilos e seu IMC é,'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
#print(nome, 'tem', altura, 'de altura,',)
#print('pesa', peso, 'quilos e seu IMC é',)
#print(imc)
