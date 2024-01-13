print('**************************************')
print('******Saiba seu IMC por aqui !!!******')
print('**************************************')
nome = input('Qual é o seu nome ? ')
idade = input('Quantos anos você tem ? ')
peso = float(input('Qual é o seu peso (kg) ? '))
altura = float(input('Digite sua altura (cm) ? '))
imc = (peso/(altura/100)**2)
print('{} seu IMC é: {:.2f}.'.format(nome,imc))

if (imc<17):
    print('Você está muito abaixo do seu peso ideal. Procure um nutricionista urgentemente!!!')
elif (imc<=18.4):
    print('Você está abaixo do seu peso ideal. Procure um nutricionista!')
elif (imc<=24.99):
    print('Você está no seu peso ideal. Continue assim!!!')
elif (imc<=29.99):
    print('Você está acima do peso seu ideal. Melhore sua dieta e faça exercícios físicos!')
elif (imc<=34.99):
    print('Você está obeso nível 1. Procure um médico e um nutricionista !!!')
elif (imc<=39.99):
    print('Você está obeso nível 2. Procure um médico e um nutricionista urgentemente!!!')
elif (imc>=40):
    print('Você está obeso nível 3. Procure um médico e um nutricionista urgentemente!!!')
