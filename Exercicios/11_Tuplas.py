# Tupla mostra números por extenso de 0 até 20

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatroze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    while numero not in range(0, 20):
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[numero]} ')
    opc = str(input('Quer continuar? [S/N]')).upper()
    if opc == 'N':
        break
print('Obrigado! Volte Sempre!')


# Tabela do Campeonato Brasileiro de Futebol
brasileirao = ('Palmeiras', 'Bragantino', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
               'Bahia', 'Santos', 'Atlético-GO', 'Ceará-SC', 'Corinthians', 'Fluminense',
               'Flamengo', 'Juventude', 'Internacional', 'Ámerica-MG', 'São Paulo',
               'Sport Recife', 'Cuiabá', 'Chapecoense', 'Grêmio')
print(f'Lista de times do Brasileirão: {brasileirao}')
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(f'O chapecoense está na {(brasileirao.index("Chapecoense")+1)}ª posição')

# Análise de dados em tuplas
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na {(numeros.index(3)+1) if 3 in numeros else 0}ª posição')
print(f'Os valores pares digitados foram: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i,end=', ')

# Lista de Preços
cont = 0
print('-'*50)
print('              LISTA DE PREÇOS')
print('-'*50)
lista=('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
      'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
      'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
while cont < len(lista):
      print(f'{lista[cont]:.<40} R$ {lista[cont + 1]:>6}')
      cont+=2
print('-'*50)

# Contador de vogais em tuplas
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for i in palavras:
      print(f'Na palavra {i} temos ', end='')
      for x in i:
            if x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
                  print(x.lower(), end=' ')
      print('')
