# Exercícos Primeiros Passos com Python

# Pergunta o nome e exibe uma mensagem de boas vindas
nome = input('Qual é o seu nome? ')
print('Olá,{}! Prazer em te conhecer!'.format(nome))

# Pergunta dia, mês e ano do nascimento e exibe em formato de data
dia = input('Qual dia do mês você nasceu? ')
mes = input('Em qual mês você nasceu? ')
ano = input('Em qual ano você nasceu? ')
print('Você nasceu no dia {} de {} de {}. Correto?'.format(dia,mes,ano))

# Pede dois números e exibe a soma entre eles
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2
print('A soma entre {} e {} é igual a: {} '.format(num1,num2,soma))
