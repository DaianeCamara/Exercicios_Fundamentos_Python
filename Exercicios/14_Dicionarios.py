# Lê nome e média de um aluno, guarda a situação em um dicionário
nota = dict()
nota['nome'] = str(input('Nome: '))
nota['média'] = float(input(f'Média de {nota["nome"]}: '))
if nota['média'] >= 7:
    nota['situação'] = 'Aprovado'
elif nota['média'] < 5:
    nota['situação'] = 'Reprovado'
else:
    nota['situação'] = 'Recuperação'
print('-='*40)
for k, v in nota.items():
    print(f'- {k} é igual a {v}')

# Jogo de Dados
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

# Cadastro de Trabalhador
import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = (datetime.date.today().year) - (int(input('Ano de Nascimento: ')))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (35 - ((datetime.date.today().year) - trabalhador['contratação'])) + trabalhador['idade']
print('-='*30)
for k,v in trabalhador.items():
    print(f'- {k} tem o valor {v} ')

# Cadastro de Jogador de Futebol
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range (0, p):
    gols.append(int(input(f'Quantos gols na patida {i}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for i, g in enumerate(gols):
    print(f'=> Na partida {i}, fez {g} gols.')
print(f'Foi um total de {sum(gols)} gols.')

# Unindo dicionários e listas
pessoas = list()
dados = dict()
total = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    while dados['sexo'] != 'M' and dados['sexo'] != 'F':
        dados['sexo'] = str(input('ERRO! Escolha apenas M ou F: ')).upper()
    dados['idade'] = int(input('Idade: '))
    total += dados['idade']
    pessoas.append(dados.copy())
    opc = str(input('Quer continuar? [S/N] ')).upper()
    while opc != 'S' and opc != 'N':
        opc = str(input('ERRO! Escolha apenas S ou N: ')).upper()
    if opc == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas. ')
print(f'B) A média de idade é de {total/len(pessoas)} anos. ')
print(f'C) As mulher(es) cadastradas foram ', end='')
for i in pessoas:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
print('')
print('D) Lista das pessoas que estão acima da média: ')
for i in pessoas:
    if i['idade'] > total/len(pessoas):
        for k, v in i.items():
            print(f'{k} = {v}', end=' ; ')
        print('')
print('<<  ENCERRADO  >>')

#  Aprimorando os Cadastro de Jogadores de Futebol
jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range (0, p):
        gols.append(int(input(f'Quantos gols na patida {i+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    opc = str(input('Quer continuar? [S/N] ')).upper()
    jogadores.append(jogador.copy())
    while opc != 'S' and opc != 'N':
        opc = str(input('ERRO! Escolha apenas S ou N: ')).upper()
    if opc == 'N':
        break
    gols.clear()
print('-=' * 30)
print('cod  nome      gols           total')
print('-'*40)
for i, j in enumerate(jogadores):
    print(f'{i:2}  {j["nome"]}  {j["gols"]}  {j["total"]}')
print('-=' * 30)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if n == 999:
        break
    elif n > len(jogadores) or n < 0:
        n = int(input('Opção inválida! Mostrar dados de qual jogador? (999 para parar) '))
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}:')
        for i, j in enumerate(jogadores[n]["gols"]):
            print(f'No jogo {i+1} fez {j} gols.')
print('-=' * 30)
print('<<<< VOLTE SEMPRE >>>>>>')