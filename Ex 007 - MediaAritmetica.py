'''
Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
'''

nota1 = float(input("Primeira nota do Aluno: "))
nota2 = float(input("Segunta nota do Aluno: "))
media = (nota1 + nota2) / 2
print(f"A média entre {nota1} e {nota2} é igual a {media:.2f}.")
