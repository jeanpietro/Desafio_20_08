# Declaração de variáveis
nome = input("Digite o seu nome: ")
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

# Imprime o tipo das variáveis
print(type(nome))
print(type(idade))
print(type(altura))
print(type(peso))

# Imprimindo as variáveis concatenadas
print(f"Olá, seu nome é {nome}, sua idade é: {idade} anos, sua altura é: {altura} m, e seu peso é: {peso} kg")

