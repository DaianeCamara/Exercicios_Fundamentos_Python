# Aprova ou não o financiamento bancário para compra de uma casa
casa = float(input('DIgite o valor do imóvel em R$'))
sal = float(input('Digite o salário do comprador em R$'))
anos = int(input('Digite o número de anos de duração do financiamento: '))
prest = (casa/(12*anos))
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prest:.2f}.')
if prest <= (sal * 0.3):
    print('Seu financiamento foi APROVADO!')
else:
    print('Seu financiamento foi NEGADO!')

#Conversor de base numérica
num1 = int(input('Digite um número inteiro: '))
conv = int(input('Escolha uma das bases para converção:\n '
                 '[1] para BINÁRIO\n [2] para OCTAL\n '
                 '[3] para HEXADECIMAL\n'
                 'Sua opção: '))
if conv == 1:
    print(f'{num1} convertido para BINÁRIO é igual a: {format(num1,"b")}')
elif conv == 2:
    print(f'{num1} convertido para OCTAL é igual a: {format(num1, "o")}')
elif conv == 3:
    print(f'{num1} convertido para HEXADECIMAL é igual a: {format(num1, "X")}')
else:
    print('Digite uma opção válida de 1 a 3.')

# Lê dois números e os compara
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
if numero1 == numero2:
    print(f'Os números digitados são iguais.')
elif numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}.')
else:
    print(f'O número {numero1} é menor que o número {numero2} .')

# Lê o ano de nascimento e mostra o ano do alistamento militar
import datetime
anon = int(input('Digite o ano do seu nascimento: '))
anoa = datetime.date.today().year
idade = anoa - anon
print(f'Quem nasceu em {anon}, tem {idade} anos em {anoa}.')
dif = (idade - 18)
if dif < 0:
    print(f'Ainda faltam {abs(dif)} ano(s) para o seu alistamento.\nSeu alistamento será em {anoa - dif}!')
elif dif == 0:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você deveria ter se alistado há {dif} anos.\nSeu alistamento foi em {anoa - dif}!')

# Calcula a média do aluno
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2
print(f'Como a primeira nota {nota1:.2f} e a segunda nota {nota2:.2f}, a média deste aluno é: {media:.2f}.')
if media >= 7:
    print('O aluno está APROVADO!')
elif media >= 5 and media <7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')

# Lê o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
import datetime
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = datetime.date.today().year - ano_nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

# Lê a medida dos segmentos e diz qual tipo de triângula eles formam
a = int(input('Digite a medida da primeira reta: '))
b = int(input('Digite a medida da segunda reta: '))
c = int(input('Digite a medida da terceira reta: '))
if ((b-c)<a<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
    if a == b == c:
        print('Essas retas podem formar um triângulo: EQUILÁTERO')
    elif a != b != c != a:
        print('Essas retas podem formar um triângulo: ESCALENO')
    else:
        print('Essas retas poderiam formar um triângulo: ISÓSCELES')
else:
    print('Essas retas não podem formar um triângulo.')

# Lê o peso e a altura de uma pessoa, calcula seu Índice de Massa Corporal (IMC) e mostra seu status
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso/(altura**2)
print(f'Seu IMC é: {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA')

# Calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
print('='*50 + 'LOJA DA DAIANE' + '='*50)
valor_da_compra = float(input('Digite o valor da compra R$'))
print('FORMAS DE PAGAMENTO:\n'
      '[1] à vista dinheiro ou cheque\n'
      '[2] à vista cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão ')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print(f'Sua compra de R${valor_da_compra:.2f} vai custar: R${(valor_da_compra*0.9):.2f}')
elif opcao == 2:
    print(f'Sua compra de R${valor_da_compra:.2f} vai custar: R${(valor_da_compra*0.95):.2f}')
elif opcao == 3:
    print(f'O valor final da sua compra é de: R${valor_da_compra:.2f} e será parcelada em 2x de R${(valor_da_compra/2):.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${((valor_da_compra*1.2)/parcelas):.2f} COM JUROS.\n'
          f'Sua compra de R${valor_da_compra:.2f} no final sairá por R${(valor_da_compra*1.2):.2f}')
else:
    print('Opção inválida, tente novamente!')

# Joga JOKENPÔ
import random
import time
print('-='*15 + 'JOKENPÔ' + '-='*15)
print('Suas opções:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
lista = ['PEDRA','PAPEL', 'TESOURA']
escolha = (int(input('Qual é a sua jogada? ')))
computador = random.choice(lista)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
time.sleep(1)
print('-='*15)
print(f'Computador jogou: {computador}')
print(f'Você jogou: {lista[escolha]}')
print('-='*15)
if lista[escolha] == computador:
    print('O jogo EMPATOU!!')
elif lista[escolha] == lista[0] and computador == lista[1]:
    print('Que pena, você PERDEU!!')
elif lista[escolha] == lista[0] and computador == lista[2]:
    print('Parabéns, você VENCEU!!')
elif lista[escolha] == lista[1] and computador == lista[0]:
      print('Parabéns, você VENCEU!!')
elif lista[escolha] == lista[1] and computador == lista[2]:
      print('Que pena, você PERDEU!!')
elif lista[escolha] == lista[2] and computador == lista[0]:
      print('Que pena, você PERDEU!!')
elif lista[escolha] == lista[2] and computador == lista[1]:
      print('Parabéns, você VENCEU!!')
else:
    print('Escola uma opção válida!')
