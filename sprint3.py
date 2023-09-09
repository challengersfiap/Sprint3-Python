# 1 – Considerando a Sprint 2 devidamente concluída, escolha e codifique ao menos 3 funcionalidades do menu, utilizando os
# conceitos aprendidos: Funções/Procedimentos, passagem de parâmetros e retorno de funções / Manipulação de estruturas de 
# dados: Listas, Tuplas, Dicionários, Tabelas (listas + dicionários).
import os
import datetime
import time
import sys

def separador(n, cor):
    limpa = '\033[0m'
    cores = {
        1: {'azul': '\033[36m', 'limpa' : limpa},
        2: {'verde': '\033[32m', 'limpa' : limpa},
        3: {'roxo' : '\033[95m' , 'limpa' : limpa},
        4: {'amarelo': '\033[33m', 'limpa': limpa},
        5: {'vermelho': '\033[31m', 'limpa': limpa},
        6: {'Lvermelho': '\033[91m', 'limpa': limpa},
        7: {'Lverde': '\033[32m', 'limpa': limpa}
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

    elif cor == 7:
        mensagem = f'{cores[7]["Lverde"]}{n}{cores[7]["limpa"]}'
    
    return mensagem

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def validacao(v, tipo, nome, cpf_formatado, dt_nasc_formatada, tel_fixo, tel_celular, email):
    if tipo == 1:
        while v not in ["1", "2", "3", "4", "5", "6"]:
            print(f"1- Nome: {nome}\n2- CPF: {cpf_formatado}\n3- Data de nascimento: {dt_nasc_formatada}\n4- Telefone fixo: {tel_fixo}\n5- Telefone celular: {tel_celular}\n6- Email: {email}")
            v = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")

        return v

def cadastroCliente():
    clear_console()
    print(separador(33, 1))
    nome = input("Digite seu nome completo: ").strip().title()

    cpf = input("Digite seu CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    cpf_formatado = formatarCpf(cpf)

    dt_nasc = input("Data de nascimento dd/mm/aaaa: ").replace("/", "").replace(" ", "")
    dt_nasc_formatada = formatarData(dt_nasc)
    tel_fixo = input("Telefone fixo(opcional): ")
    tel_celular = input("Celular(opcional): ")
    email = input("Informe seu email: ")
    clear_console()
    print(separador(33,1))
    clear_console()
    print(separador(33,1 ))
    print(f"1- Nome: {nome}\n2- CPF: {cpf_formatado}\n3- Data de nascimento: {dt_nasc_formatada}\n4- Telefone fixo: {tel_fixo}\n5- Telefone celular: {tel_celular}\n6- Email: {email}")
    print(separador(33, 1))

    mudanca = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")
    while mudanca != "0":
        if mudanca == "1":
            nome = input("Nome: ").strip().title()

        elif mudanca == "2":
            cpf = input("CPF: ")
            cpf_formatado = formatarCpf(cpf)

        elif mudanca == "3":
            dt_nasc = input("Data de nascimento: ")
            dt_nasc_formatada = formatarData(dt_nasc)

        elif mudanca == "4": 
            tel_fixo = input("Telefone fixo: ")

        elif mudanca == "5":
            tel_celular = input("Celular: ")

        elif mudanca == "6":
            email = input("Email: ")
        clear_console()
        print(separador(33,1 ))
        print(f"1- Nome: {nome}\n2- CPF: {cpf_formatado}\n3- Data de nascimento: {dt_nasc_formatada}\n4- Telefone fixo: {tel_fixo}\n5- Telefone celular: {tel_celular}\n6- Email: {email}")
        print(separador(33, 1))
        mudanca = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")

    print("Validando dados", end="")
    for c in range(3):
        time.sleep(0.7)
        print(".", end="")
        sys.stdout.flush()
    print("Dados aprovados!")
    time.sleep(3)
    infos = [nome, cpf_formatado, dt_nasc_formatada, tel_fixo, tel_celular, email]
    return infos
    

def formatarCpf(cpf):
    while len(cpf) > 11 or len(cpf) < 11:
        print(separador("CPF inválido!", 6), end="")
        cpf = input(f", deve conter 11 caracteres\nDigite seu CPF: ").replace(".", "").replace("-", "").replace(" ", "")
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def formatarData(data):
    while True:
        if len(data) != 8:
            print(separador("Erro!", 6), end="")
            data = input(" Quantidades de caracteres diferente de 8!\nData de nascimento dd/mm/aaaa: ").replace("/", "").replace(" ", "")
            continue 

        data_atual = datetime.date.today()
        data_nascimento = datetime.date(int(data[4:]), int(data[2:4]), int(data[:2]))
        mes_nascimento = int(data[2:4])
        dia_nascimento = int(data[:2])
        idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (mes_nascimento, dia_nascimento))

        if 18 <= idade <= 100:
            break 

        if idade < 18:
            print(separador("Você é menor de idade!", 6))
        elif idade > 100:
            print(separador("Você tem mais de 100 anos!", 6))

        data = input("Data de nascimento: ")  # Recalcule a idade após a entrada da data

    return f'{data[:2]}/{data[2:4]}/{data[4:]}'

def bike():
    clear_console()
    print(separador(33, 3))
    print("Cadastro da bike")
    n_serie = input("Número de série:")
    valor = input("Valor da bike: R$")
    cor = input("Cor: ")
    modelo = input("Modelo: ")

#Programa principal
cadastroCliente()