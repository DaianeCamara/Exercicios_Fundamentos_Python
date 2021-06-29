# Mostra todas as letras maiúsculas, minúsculas e número de letras do primeiro nome
nome = str(input('Qual seu nome completo? ')).strip()
nomeu = nome.upper()
print(f'Nome em maiúsculas: {nomeu}')
nomel = nome.lower()
print(f'Nome em minúsculas: {nomel}')
nomec = len(nome) - nome.count(' ')
print(f'Quantas letras tem o nome completo: {nomec}')
nomep = nome.find(' ')
print(f'Quantas letras tem o primeiro nome: {nomep}')

# Lê o nome de uma cidade e diz se ela começa ou não com santo
cidade = str(input('Digite o nome da cidade onde você nasceu: ')).strip().lower()
cid = (cidade.split(' '))
cids = str(cid[0])
print(cids == 'santo')

# Lê o nome de uma pessoa e diz se tem silva no nome
nm = str(input('Digite seu nome completo: ')).strip().lower()
print('Seu nome tem silva: ', end=' ')
print(' silva ' in nm)

# Lê uma frase e mostra o número de ocorrências de uma string a primeira e ultima posição de ocorrência
frase = str(input('Digite uma frase: ')).strip().lower()
numa = frase.count('a')
print(f'A letra A aparece {numa} vez(es) na frase.')
prim = frase.find('a') + 1
print(f'A primeira letra A aparece na {prim} posição .')
ult = frase.rfind('a') + 1
print(f'A última letra A aparece na {ult} posição .')

# Lê o nome, mostra o primeiro e último nome e uma saudação
nom1 = str(input('Qual seu nome completo? ')).strip().title().split(' ')
print('Muito prazer em te conhecer!')
pnom = nom1[0]
print(f'Seu primeiro nome é: {pnom}')
unom = nom1[-1]
print(f'Seu último nome é: {unom}')