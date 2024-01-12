print('*****************************************')
print('************JOGO DA ADVINHAÇÃO***********')
print('*****************************************')
numero = 47
chute = int(input('Chute um número: '))
print('Você digitou {}' .format(chute))
if numero == chute:
    print('Você acertou')
elif chute < numero:
    print('Você errou, seu chute foi menor que o número certo')
elif chute > numero:
    print('Você errou, seu chute foi maior que o número certo')
    