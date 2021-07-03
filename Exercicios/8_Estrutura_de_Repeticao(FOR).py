# Contador regressivo
import time
for c in range(10,-1,-1):
    print(c)
    time.sleep(0.5)
print('BUM! BUM! POOOW!')

# Mostra na tela todos os números pares que estão no intervalo entre 1 e 50
for par in range(2,51,2):
    print(par, end =' ')
print('ACABOU!')

# Calcula a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for mult in range(0,501,3):
    if mult % 2 == 1:
        soma += mult
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é: {soma}')

# Tabuada 2.0
n = int(input('Digite um número: '))
for tab in range(1,11):
    print(f'{n} x {tab:2} = {n*tab}')

# Lê seis números inteiros e mostra a soma apenas daqueles que forem pares
soma = 0
contagem = 0
for nums in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        contagem += 1
print(f'Você informou {contagem} números pares e a soma é: {soma}')

# Lê o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos dessa progressão
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for prog in range(termo,(10*razao),razao):
    print(prog, end=' → ')
print('ACABOU')

# Lê um número inteiro e mostra se ele é ou não um número primo
numero = int(input('Digite um número: '))
cont = 0
for primo in range(1,(numero+1)):
    print(primo, end=' ')
    if numero % primo ==0:
        cont += 1
print(f'\nO número {numero}, foi divisível {cont} vezes')
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')

# Lê uma frase qualquer e diz se ela é um palíndromo
frase = str(input('Digite uma frase: ')).upper().replace(' ','')
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')

# Lê o ano de nascimento de sete pessoas, mostra quantas pessoas tem mais e menos de 18 anos
import datetime
contagem = 0
CONTAGEM = 0
for pessoa in range(1,8):
    ano = (int(input(f'Em que ano a {pessoa}ª pessoa nasceu? ')))
    if (datetime.date.today().year - ano) < 18:
        contagem += 1
    else:
        CONTAGEM += 1
print(f'Ao todo tivemos {CONTAGEM} pessoas maiores de idade\n'
      f'E também tivemos {contagem} pessoas menores de idade')

# Lê o peso de cinco pessoas e mostra qual foi o maior e o menor peso lidos
peso = []
for pes in range(1,6):
    peso.append(float(int(input(f'Peso da {pes}ª pessoa: '))))
print(f'O maior peso lido foi de {max(peso)}Kg')
print(f'O menor peso lido foi de {min(peso)}Kg')

