# Jogo de advinhação
import random
import time
numpc = random.randint(0,5)
numus = int(input('De 0 a 5, adivinhe em qual número eu pensei? '))
print('Processando ...')
time.sleep(3)
if numpc == numus:
    print('Parabéns você acertou!')
else:
    print(f'Que pena você errou!\nO número que pensei foi: {numpc}')

# Calcula multa por excesso de velocidade
vel = float(input('Digite a velocidade do carro em Km/h: '))
multa = (vel-80)*7
if vel <= 80:
    print('Parabéns, você está dentro do limite de velocidade!')
else:
    print(f'MULTADO! Você excedeu o limite de 80Km/h e o valor da multa é R${multa:.2f}')

# Lê um número e diz se ele é par ou ímpar
numero = int(input('Digite um número: '))
divisao = numero % 2
if divisao == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

# Calcula o custo da viagem
dist = float(input('Qual foi a distância percorrida na viagem em Km: '))
if dist <= 200:
    print(f'O custo da sua viagem foi de R${dist*0.5:.2f}.')
else:
    print(f'O custo da sua viagem foi de R${dist*0.45:.2f}.')

# Mostra o maior e menor valor digitado
lista = []
lista.append(int(input('Digite o primeiro valor: ')))
lista.append(int(input('Digite o segundo valor: ')))
lista.append(int(input('Digite o terceiro valor: ')))
print(f'O maior valor digitado foi: {max(lista)}')
print(f'O menor valor digitado foi: {min(lista)}')

# Calcula diferente reajuste para diferentes faixas salariais
sal = float(input('Digite o salário do funcionário R$'))
if sal <= 1250:
   nsal = sal * 1.15
else:
    nsal = sal * 1.1
print(f'O salário foi reajustado de R${sal:.2f} para R${nsal:.2f}. ')

# Lê a medida de 3 retas e diz se podem formar um triângulo
a = int(input('Digite a medida da primeira reta: '))
b = int(input('Digite a medida da segunda reta: '))
c = int(input('Digite a medida da terceira reta: '))
if ((b-c)<a<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
    print('Essas retas poderiam formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
