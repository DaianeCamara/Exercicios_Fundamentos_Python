# Lê um número real e mostra sua parte inteira
import math
n = float(input('Digite um número inteiro:'))
print('A parte inteira de {} é {}.'.format(n, math.trunc(n)))

# Calcula a hipotenusa
import math
o = float(input('Digite a medida do cateto oposto: '))
a = float(input('Digite a medida do cateto adjacente: '))
h = math.hypot(o, a)
print(f'Para o cateto adjacente {a} e para o cateto oposto {o} o valor da hipotenusa é: {h:.2f}')

# Calcula seno e cosseno
import math
angulo = float(input('Digite o ângulo: '))
print(f'O seno do ângulo {angulo} é: {math.sin(math.radians(angulo)):.2f}'
      f'\nO cosseno do ângulo {angulo} é: {math.cos(math.radians(angulo)):.2f}'
      f'\nA tangente do ângulo {angulo} é: {math.tan(math.radians(angulo)):.2f}')

# Sorteia um nome aleatório
import random
a1 = str(input('Digite o nome o nome do primeiro aluno: '))
a2 = str(input('Digite o nome o nome do segundo aluno: '))
a3 = str(input('Digite o nome o nome do terceiro aluno: '))
a4 = str(input('Digite o nome o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)
print(f'O aluno escolhido foi: {escolhido}')

# Exibe uma ordem aleatória para os elementos da lista
import random
n1 = str(input('Digite o nome o nome do primeiro aluno: '))
n2 = str(input('Digite o nome o nome do segundo aluno: '))
n3 = str(input('Digite o nome o nome do terceiro aluno: '))
n4 = str(input('Digite o nome o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação é:\n{lista}')

#Abre e reproduz um áudio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

