# Exemplo:
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# Lê e guarda em uma lista 5 valores numéricos, mostra o maior e o menor valor e suas respectivas posições na lista.
lista = []
p = 0
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))
print('=-'*40)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        p += i
        print(f'{p}...',end='')
print('')
print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        p += i
        print(f'{p}...', end='')

# Valores únicos em uma Lista
opc = ''
numeros=[]
while opc != 'N':
    n = (int(input('Digite um valor: ')))
    if n in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    opc = str(input('Quer continuar? [S/N] ')).upper()
print('-='*40)
print(f'Você digitou os valores {sorted(numeros)}')

# Lista ordenada sem repetições
lista = []
n = int(input('Digite um número: '))
lista.append(n)
print('Adicionado ao final da lista...')
for i in range(0,4):
    n = int(input('Digite um número: '))
    if n > max(lista):
        print('Adicionado ao final da lista...')
        lista.append(n)
    elif n < min(lista):
        print('Adicionado na posição 0 da lista...')
        lista.insert(0,n)
    else:
        for index, valor in enumerate(lista[:]):
            if n < valor:
                lista.insert(index,n)
                print(f'Adicionado na posição {index} da lista')
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')

# Extraindo dados de uma Lista
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opc = str(input('Quer continuar? [S/N] ')).upper()
    if opc == 'N':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
print(f'O valor 5 faz parte da lista.' if 5 in lista else 'O valor 5 não está presente na lista.')

# Dividindo valores em várias listas
lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    opc = str(input('Quer continuar? [S/N] ')).upper()
    if opc == 'N':
        break
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}'if len(pares) > 0 else 'Não há números pares na lista.')
print(f'A lista de ímpares é {impares}' if len(impares) > 0 else 'Não há números ímpares na lista.')
