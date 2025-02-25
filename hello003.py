"""
Programa: Hello
Descrição: imprima na tela a frase "Hello, World!"
Autor: Filipe Eich
Data: 25/02/2025
Versao: 0.0.3

25/02/2025
1. Nesta versão, o usuário poderá entrar com seu nome para ser cumprimentado pelo programa.
"""

#Alocaçao de memoria

nome_usuario=""

frase = "Hello, "

#Entrada de dados

nome_usuario = input("\nQual o seu nome: ")


#Processamento de dados

frase = frase + nome_usuario


#Saida de dados


print(frase)


