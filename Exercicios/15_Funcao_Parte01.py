# Função que calcula área


def area(larg, comp):
    ar = larg * comp
    print(f'A área de um terreno {larg} é {comp} de {ar}m²')


print('      Controle de terreno')
print('-' * 40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

# Um print especial


def escreva(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


escreva('Johnatas eu te amo!')

# Função de Contador


def contador(a, b, c):
    print('-='*30)
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if a < b:
        for i in range(a, b+1, abs(c)):
            print(i, end=' ')
    else:
        for i in range(a, b-1, -abs(c)):
            print(i, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

# Função que descobre o maior


def maior_valor(* n):
    print('-='*30)
    print('Analisando os valores passados...')
    for i in n:
        print(i, end=' ')
    print(f'Foram informados {len(n)} valores ao todo. ')
    if len(n) > 0:
        print(f'O maior valor informado foi {max(n)} ')


maior_valor(5, 3, 8, 10, 9)
maior_valor()

# Funções para sortear e somar
from random import randint


def soma_par(* n):
    soma = 0
    for i in n:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {n}, temos {soma}')


def lista_sorteada():
    valores = []
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        valores.append(n)
    print('PRONTO!')
    soma_par(*valores)


lista_sorteada()
