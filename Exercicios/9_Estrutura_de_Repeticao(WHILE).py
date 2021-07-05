# Lê o sexo de uma pessoa, mas só aceita os valores ‘M’ ou ‘F’
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print(f'Sexo {sexo} registrado com sucesso!')

# Jogo de Adivinhação
import random
cont = 1
print('Sou seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual f   oi?')
computador = random.randint(0, 10)
palpite = int(input('Qual é seu palpite? '))
while computador != palpite:
    cont += 1
    if computador < palpite:
        print('Menos... Tente mais uma vez! ')
    elif computador > palpite:
        print('Mais... Tente mais uma vez! ')
    palpite = int(input('Qual é seu palpite? '))
print(f'Acertou com {cont} tentativas. Parabéns!')

#  Lê dois valores e mostra opções de operações matemáticas
import time
primeiro_numero = int(input('Primeiro valor: '))
segundo_numero = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        print(f'A soma entre {primeiro_numero} + {segundo_numero} é {primeiro_numero + segundo_numero}')
    elif opcao == 2:
        print(f'A multiplicação entre {primeiro_numero} x {segundo_numero} é {primeiro_numero * segundo_numero}')
    elif opcao == 3:
        print(f'O maior número entre {primeiro_numero} e {segundo_numero} é {max(primeiro_numero,segundo_numero)}')
    elif opcao == 4:
        primeiro_numero = int(input('Primeiro valor: '))
        segundo_numero = int(input('Segundo valor: '))
    elif opcao > 5 or opcao == 0:
        print('Escolha uma opção válida!')
print('Finalizando o programa ...')
time.sleep(2)
print('Obrigado e Volte Sempre!!')

# Lê o primeiro termo e a razão de uma PA, mostra os 10 primeiros termos da progressão
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
while primeiro_termo <= razao*10:
    print(primeiro_termo, end=' → ')
    primeiro_termo += razao
print('FIM')

#Lê o primeiro termo e a razão de uma PA, mostra os 10 primeiros termos da progressão e pergunta para o usuário se ele quer mostrar mais alguns termos.
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termos = 10
digitados = termos
while digitados != 0:
    while primeiro_termo <= razao*termos:
        print(primeiro_termo, end=' → ')
        primeiro_termo += razao
    print('PAUSA')
    digitados = int(input('Quantos termos a mais você quer mostrar? '))
    termos += digitados
print(f'Finalizando o programa...\nForam mostrados {termos} termos.\nFIM!!!')

# Sequência de Fibonacci
print('~'*100)
print('                         SEQUÊNCIA DE FIBONACCI')
print('~'*100)
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*100)
num0 = 0
num1 = 1
cont = 3
print(f'{num0} → {num1}', end=' → ')
while cont <= termos:
    num2 = num0 + num1
    num0 = num1
    num1 = num2
    print(num2, end=' → ')
    cont += 1
print('FIM')

# Soma todos os números inteiros digitados e para sair  digitar 999(excluindo-o do somatório)
n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi: {soma}')

# Lê vários números inteiros pelo teclado, mostra a média entre eles e qual foi o maior e o menor valores lidos
opcao = 'x'
soma = 0
cont = 1
maior = 0
menor = 0
num = int(input('Digite um número: '))
if cont == 1:
    maior = num
    menor = num
soma += num
while opcao != 'N':
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'S':
        num = int(input('Digite um número: '))
        if cont == 0:
            maior = menor = num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        soma += num
        cont += 1
    elif opcao != 'N':
        print('Opção INVÁLIDA...Digite [S/N]: ')
print(f'Você digitou {cont} números e a média foi: {soma/cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
