# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota,
#  a menor nota e a média das notas.

notas = []
for i in range(5):
    nota = float(input("Digite a nota dos alunos: "))
    notas.append(nota)

maior_nota = max(notas)
menor_nota = min(notas)
media_notas = sum(notas) / 5

print("maior nota", maior_nota)
print("menor nota", menor_nota)
print("média das notas", media_notas)

