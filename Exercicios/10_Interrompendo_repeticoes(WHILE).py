# Lê números inteiros, para quando o usuário digitar o valor 999 e mostre quantos números foram digitados e a soma entre eles
cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números foi {soma}.')

# Mostra a tabuada, uma de cada vez, para cada valor digitado pelo usuário, o programa é interrompido quando o número solicitado for negativo.
while True:
    print('-'*100)
    tabuada = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 100)
    mult = cont = 0
    if tabuada < 0:
        break
    while mult < (tabuada*10):
        cont += 1
        mult = tabuada * cont
        print(f'{tabuada} x {cont:2} = {mult}')
print('Tabuada encerrada, volte sempre!')

# Joga par ou ímpar
import random
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    opc = str(input('Par ou Ímpar? [P/I] ')).upper()
    comp = random.randint(1,10)
    if ((valor + comp) % 2) == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'Você jogou {valor} e o computador {comp}. Total de {valor + comp} ', end='')
    print('DEU PAR' if ((valor + comp) % 2) == 0 else 'DEU ÍMPAR')
    if opc == resultado:
        cont += 1
        print('Você VENCEU!\nVamos jogar novamente...')
    else:
        break
print(f'Você PERDEU!\nGAME OVER! Você venceu {cont} vez(es).')

# Lê a idade e o sexo de várias pessoas, mostra quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados,quantas mulheres tem menos de 20 anos.
print('-'*100)
print('Cadastre uma pessoa')
print('-'*100)
maior = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Digite uma opção válida!\nSexo: [M/F] ')). upper()
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher += 1
    print('-' * 100)
    opc = str(input('Quer continuar? [S/N] ')).upper()
    while opc not in 'SN':
        opc = str(input('Digite uma opção válida!\nQuer continuar? [S/N]  ')). upper()
    if opc == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homem(ns) cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 20 anos.')

# Lê o nome e o preço de vários produtos, mostra total da compra, quantos produtos custam mais de R$1000 e qual é o nome do produto mais barato.
print('-' * 50)
print('LOJA SUPER BARATÃO')
print('-' * 50)
total = produto = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000.00:
        produto += 1
    if cont == 0:
        menor = preco
        barato = nome
    if preco < menor:
        menor = preco
        barato = nome
    cont += 1
    opc = str(input('Quer continuar? [S/N] ')).upper()
    while opc not in 'SN':
        opc = str(input('Opção INVÁLIDA!!\nQuer continuar? [S/N] ')).upper()
    if opc == 'N':
        break
print('-'*17 + 'FIM DO PROGRAMA' + '-' *17)
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {produto} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

# Simule o funcionamento de um caixa eletrônico
print('='*50)
print('             BANCO BAMERINDOS')
print('='*50)
valor = int(input('Que valor você quer sacar? R$'))
while valor // 50 > 0:
    print(f'Total de {valor // 50} cédulas de R$50')
    valor -= 50 * (valor // 50)
while valor // 10 > 0:
    print(f'Total de {valor // 10} cédulas de R$10')
    valor -= 10 * (valor // 10)
while valor // 1 > 0:
    print(f'Total de {valor // 1} cédulas de R$1')
    valor -= 1 * (valor // 1)
print('='*50)
print('Volte sempre ao BANCO BAMERINDOS! Tenha um bom dia!')
