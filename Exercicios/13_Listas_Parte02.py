# Lista composta e análise de dados
nome_peso = []
pessoas = []
p_p = []
p_l = []
while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(float(input('Peso [Kg]: ')))
    opc = str(input('Quer continuar? [S/N] ')).upper()
    pessoas.append(nome_peso[:])
    nome_peso.clear()
    if opc == 'N':
        break
print(pessoas)
for p in pessoas:
    if p[1] == max(pessoas)[1]:
        p_p.append(p[0])
    if p[1] == min(pessoas)[1]:
        p_l.append(p[0])
print('-='*40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {max(pessoas)[1]}Kg. Peso de {p_p}')
print(f'O menor peso foi de {min(pessoas)[1]}Kg. Peso de {p_l}')

# Listas com pares e ímpares
numeros = [[], []]
for i in range(1,8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')

# Matriz em Python
somap = somac = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0, 3):
    for x in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {x}]: '))
        matriz[i][x] = n
        if n % 2 == 0:
            somap += n
        if x == 2:
            somac += n
print('-='*30)
# print(matriz)
for m in matriz:
    for y in m:
        print(f'[{y:^5}]', end='')
    print('')
print('-='*30)
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print('-='*30)

# Sorteia os números da mega sena
import random
combo = list()
palpite = list()
print('-'*60)
print('                  JOGA NA MEGA SENA')
print('-'*60)
sort = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3 + f'   SORTEANDO {sort} JOGOS   '+ '-='*3)
for i in range(1,sort+1):
    print(f'Jogo {i}: ', end='')
    while len(palpite) < 6:
        n = random.randint(1,60)
        if n not in palpite:
            palpite.append(n)
    combo.append(palpite[:])
    print(sorted(palpite))
    palpite.clear()
print('-='*3 + ' *  BOA SORTE  * '+ '-='*3)

# Boletim com listas compostas
classe = list()
alunos = list()
cont = 0
while True:
    alunos.append(str(input('Nome: ')))
    alunos.append((input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    opc = str(input('Quer continuar? [S/N] ')).upper()
    classe.append(alunos[:])
    alunos.clear()
    if opc == 'N':
        break
print('-='*35)
print('Nº  Nome        Média')
print('-'*25)
for i, n in enumerate(classe):
    print(f'{i:2}   {classe[cont][0]:<10} {(float(classe[cont][1]) + float(classe[cont][2]))/2:.1f}')
    cont += 1
print('-'*25)
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if escolha == 999:
        break
    print(f'As notas de {classe[escolha][0]} são {float(classe[escolha][1]):.1f} e {float(classe[escolha][2]):.1f}')
print('-------   VOLTE SEMPRE   ------')
