# 1 – Considerando a Sprint 2 devidamente concluída, escolha e codifique ao menos 3 funcionalidades do menu, utilizando os
# conceitos aprendidos: Funções/Procedimentos, passagem de parâmetros e retorno de funções / Manipulação de estruturas de 
# dados: Listas, Tuplas, Dicionários, Tabelas (listas + dicionários).
import os

def separador(n, cor):
    limpa = '\033[0m'
    cores = {
        1: {'azul': '\033[36m', 'limpa' : limpa},
        2: {'verde': '\033[32m', 'limpa' : limpa},
        3: {'roxo' : '\033[95m' , 'limpa' : limpa},
        4: {'amarelo': '\033[33m', 'limpa': limpa},
        5: {'vermelho': '\033[31m', 'limpa': limpa},
        6: {'Lvermelho': '\033[91m', 'limpa': limpa}
    }

    if cor == 1:
        mensagem = f'{cores[1]["azul"]}-={cores[1]["limpa"]}' * n

    elif cor == 2:
        mensagem = f'{cores[2]["verde"]}-={cores[2]["limpa"]}' * n

    elif cor == 3:
        mensagem = f'{cores[3]["roxo"]}-={cores[3]["limpa"]}' * n

    elif cor == 5:
        mensagem = f'{cores[5]["vermelho"]}-={cores[5]["limpa"]}' * n

    elif cor == 4:
        mensagem = f'{cores[4]["amarelo"]}-={cores[4]["limpa"]}' * n

    elif cor == 6:
        mensagem = f'{cores[6]["Lvermelho"]}{n}{cores[6]["limpa"]}'
    
    return mensagem

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def cadastroCliente():
    clear_console()
    print(separador(33, 1))
    nome = input("Digite seu nome completo: ")

    cpf = input("Digite seu CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    cpf_formatado = formatarCpf(cpf)

    dt_nasc = input("Data de nascimento dd/mm/aaaa: ").replace("/", "").replace(" ", "")
    dt_nasc_formatada = formatarData(dt_nasc)
    tel_fixo = input("Telefone fixo(opcional): ")
    tel_celular = input("Celular(opcional): ")
    email = input("Informe seu email: ")
    clear_console()
    print(separador(33,1))
    print(f"Nome: {nome}\nCPF: {cpf_formatado}\nData de nascimento: {dt_nasc_formatada}")

def formatarCpf(cpf):
    while len(cpf) > 11 or len(cpf) < 11:
        print(separador("CPF inválido!", 6), end="")
        cpf = input(f", deve conter 11 caracteres\nDigite seu CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def formatarData(data):
    while len(data) > 8 or len(data) < 8:
        print(separador("Erro!", 6), end="")
        data = input(" Quantidades de caracteres diferente de 8!\nData de nascimento dd/mm/aaaa: ").replace("/", "").replace(" ", "")
    
    return f'{data[:2]}/{data[2:4]}/{data[4:]}'


#Programa principal
cadastroCliente()