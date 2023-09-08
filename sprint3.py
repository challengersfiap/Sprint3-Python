# 1 – Considerando a Sprint 2 devidamente concluída, escolha e codifique ao menos 3 funcionalidades do menu, utilizando os
# conceitos aprendidos: Funções/Procedimentos, passagem de parâmetros e retorno de funções / Manipulação de estruturas de 
# dados: Listas, Tuplas, Dicionários, Tabelas (listas + dicionários).
import os

def separador(n, cor):
    cores = {
        1: {'azul': '\033[36m', 'limpa' : '\033[0m'},
        2: {'verde': '\033[32m', 'limpa' : '\033[0m'},
        3: {'roxo' : '\033[95m' , 'limpa' : '\033[0m'},
        4: {'amarelo': '\033[33m', 'limpa': '\033[0m'},
        5: {'vermelho': '\033[31m', 'limpa': '\033[0m'}
    }

    if cor == 1:
        mensagem = print(f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n)

    elif cor == 2:
        mensagem = print(f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n)

    elif cor == 3:
        mensagem = print(f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n)

    elif cor == 5:
        mensagem = print(f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n)

    else:
        mensagem = print(f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n)
    return mensagem

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def cadastroCliente():
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    dt_nasc = input("Informe a sua data de nascimento: ")
    tel_fixo = input("Telefone fixo(opcional): ")
    tel_celular = input("Celular(opcional): ")
    email = input("Informe seu email: ")
    print(cpf)

#Programa principal
cadastroCliente()