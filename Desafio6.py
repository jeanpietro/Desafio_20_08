# Declaração de variável
nota1 = input('Primeira nota do aluno: ')
nota2 = input('Segunda nota do aluno: ')
nota3 = input('Terceira nota do aluno: ')
nota4 = input('Quarta nota do aluno: ')
nota5 = input('Quinta nota do aluno: ')

# Conversão dos valores
nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
nota4 = int(nota4)
nota5 = int(nota5)

# Cálculo da média
media = (nota1+nota2+nota3+nota4+nota5)/5

# Imprime a média dos alunos
print(f'A média dos alunos é igual a: {media}')