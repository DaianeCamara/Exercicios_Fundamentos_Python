# Exercícios sobre Operadores Aritiméticos

# Mostra o antecessor e o sucessor do número digitado
n1 = int(input('Digite um número: '))
print('O antecessor é: {}'.format(n1-1))
print('O sucessor é: {}'.format(n1+1))

# Mostra o dobro, triplo e a raiz quadrada do número digitado
n2 = int(input('Digite um número: '))
print('O dobro é: {}'.format(n2*2))
print('O triplo é: {}'.format(n2*3))
print('A raiz quadrada é: {}'.format(n2**(1/2)))

# Pede duas notas e exibe a média do aluno
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
print('A média do aluno é: {}'.format((nota1+nota2)/2))

# Converte medida em metros para cm e mm
a = float(input('Digite sua altura em metros: '))
print('Sua altura em centimentos é: {:.0f} \nSua altura em milímetros é: {:.0f}'.format((a*100),(a*1000)))

# Mostra a tabuada do número digitado
nt = int(input('Digite um número: '))
print('A tabulada de {} é: '.format(nt))
print('{} x {:2} = {}'.format(nt, 1, (nt*1)))
print('{} x {:2} = {}'.format(nt, 2, (nt*2)))
print('{} x {:2} = {}'.format(nt, 3, (nt*3)))
print('{} x {:2} = {}'.format(nt, 4, (nt*4)))
print('{} x {:2} = {}'.format(nt, 5, (nt*5)))
print('{} x {:2} = {}'.format(nt, 6, (nt*6)))
print('{} x {:2} = {}'.format(nt, 7, (nt*7)))
print('{} x {:2} = {}'.format(nt, 8, (nt*8)))
print('{} x {:2} = {}'.format(nt, 9, (nt*9)))
print('{} x {:2} = {}'.format(nt, 10, (nt*10)))

# Conversor de real para dólar
real = float(input('Quanto dinheiro você tem na carteira? '))
print('Você pode comprar US${:.2f}'.format(real/3.27))

# Calcula a quantidade de tinta necessária
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
print('Sua parede tem uma área de {}m2 \nVocê precisará de {}L de tinta'.format((altura*largura),((altura*largura)/2)))

# Calcula o desconto
p = float(input('Digite o valor do produto: '))
print('O valor do produto com 5% de desconto é R${:.2f}.'.format(p*0.95))

# Calcula o reajuste salarial
s = float(input('Digite o salário atual: R$'))
print('O novo salário com reajuste de 15% é R${:.2f}.'.format(s*1.15))

# Converte a temperatura de Celsius para Fahrenheit
t = float(input('Digite a temperatura em graus Celsius: '))
f = (t*(9/5))+32
print('A temperatura em Fahrenheit é {:.1f}°F'.format(f))

# Calcula valor a pagar de um carro alugado
km = float(input('Quantos Km foram percorridos com o carro? '))
d = int(input('Quantos dias o carro ficou alugado? '))
v = (km*0.15)+(d*60)
print(' O valor total a ser pago é de R${:.2f}.'.format(v))
