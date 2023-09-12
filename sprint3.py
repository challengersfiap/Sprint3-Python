import os
import datetime
import time
import sys
import webbrowser

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
    os.system('cls' if os.name == 'nt' else 'clear')

def validacao(v, tipo, var):
    if tipo == 1:
        while v not in ["0", "1", "2", "3", "4", "5", "6"]:
            clear_console()
            print(separador(33, 1))
            print(separador("Opção inválida!", 6))
            print(f"1- Nome: {var[0]}\n2- CPF: {var[1]}\n3- Data de nascimento: {var[2]}\n4- Telefone fixo: {var[2]}\n5- Telefone celular: {var[4]}\n6- Email: {var[5]}")
            print(separador(33, 1))
            v = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")
        return v

    elif tipo == 2:
        while v not in ["1", "2", "3"]:
            clear_console()
            print(separador(33, 1))
            print(separador("Opção inválida!", 6))
            v = input("1- Fazer seguro de bike!\n2- Saber informações do seguro\n3- Sair").strip()        
        return v

    elif tipo == 3:
        while v not in ["0", "1", "2", "3", "4"]:
            clear_console()
            print(separador(33,3))
            print(separador("Opção inválida!", 6))
            print(f"1- Número de série: {var[0]}\n2- Valor: R${var[1]:,.2f}\n3- Cor: {var[2]}\n4- Modelo: {var[3]}")
            print(separador(33, 3))
            v = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")
        return v
    
    elif tipo == 4:
        while v not in ["1", "2", "3"]:
            clear_console()
            print(separador(33, 2))
            print(separador("Opção inválida!", 6))
            v = input("1- Fazer seguro de bike\n2- Saber sobre o seguro de bike\n3- Sair\n")
        return v
    
    elif tipo == 5:
        while v not in ["S", "N"]:
            clear_console()
            print(separador(33, 2))
            print(separador("Opção inválida!", 6))
            v = input("A bike possui algum dano estético?[S/N] ").strip().upper()
        return v
    
    elif tipo == 6:
        while v not in ["S", "N"]:
            clear_console()
            print(separador(33, 2))
            print(separador("Opção inválida!", 6))
            v = input("A bike possui algum dano que afete o funcionamento? [S/N] ").replace(" ", "").upper()
        return v
def menuPrincipal():
    print(separador(33, 4))
    option = input("1- Fazer seguro de bike!\n2- Saber informações do seguro\n3- Sair").strip()
    option = validacao()
    return option

def cadastroCliente():
    dados = []
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

    addLista(dados, nome, cpf_formatado, dt_nasc_formatada, tel_fixo, tel_celular, email)

    clear_console()
    print(separador(33,1))
    clear_console()
    print(separador(33,1 ))
    print(f"1- Nome: {dados[0]}\n2- CPF: {dados[1]}\n3- Data de nascimento: {dados[2]}\n4- Telefone fixo: {dados[3]}\n5- Telefone celular: {dados[4]}\n6- Email: {dados[5]}")
    print(separador(33, 1))

    mudanca = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")
    while mudanca != "0":
        mudanca = validacao(mudanca, 1, dados)
        if mudanca == "1":
            dados[0] = input("Nome: ").strip().title()

        elif mudanca == "2":
            cpf = input("CPF: ")
            dados[1] = formatarCpf(cpf)

        elif mudanca == "3":
            dt_nasc = input("Data de nascimento: ")
            dados[2] = formatarData(dt_nasc)

        elif mudanca == "4": 
            dados[3] = input("Telefone fixo: ")

        elif mudanca == "5":
            dados[4] = input("Celular: ")

        elif mudanca == "6":
            dados[5] = input("Email: ")

        clear_console()
        print(separador(33,1 ))
        print(f"1- Nome: {dados[0]}\n2- CPF: {dados[1]}\n3- Data de nascimento: {dados[2]}\n4- Telefone fixo: {dados[3]}\n5- Telefone celular: {dados[4]}\n6- Email: {dados[5]}")
        print(separador(33, 1))
        mudanca = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")
        validacao(mudanca, 1, dados)

    print("Validando dados", end="")
    for c in range(3):
        time.sleep(0.7)
        print(".", end="")
        sys.stdout.flush()
    print("\n\x1b[32mDados aprovados!\x1b[0m")
    time.sleep(3)
    return dados
    
def bike():
    dados = []
    clear_console()
    print(separador(33, 3))
    print("Cadastro da bike!")
    n_serie = input("Número de série (11 caracteres):")
    n_serie_validado = validarNserie(n_serie)
    valor = validaValor()
    cor = input("Cor: ")
    modelo = input("Modelo: ")

    addLista(dados, n_serie_validado, valor, cor, modelo)

    clear_console()
    print(separador(33, 3))
    print(f"1- Número de série: {dados[0]}\n2- Valor: R${dados[1]:,.2f}\n3- Cor: {dados[2]}\n4- Modelo: {dados[3]}")
    print(separador(33, 3))
    mudanca = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")
    while mudanca != "0":
        mudanca = validacao(mudanca, 3, dados)
        if mudanca == "1":
            n_serie = input("Número de série (11 caracteres): ")
            dados[0] = validarNserie(n_serie)
            # dados[0] = n_serie_validado
        
        elif mudanca == "2":
            dados[1] = validaValor()
        
        elif mudanca == "3":
            dados[2] = input("Cor: ")

        elif mudanca == "4":
            dados[3] = input("Modelo: ")
        
        clear_console()
        print(separador(33, 3))
        print(f"1- Número de série: {dados[0]}\n2- Valor: R${dados[1]:,.2f}\n3- Cor: {dados[2]}\n4- Modelo: {dados[3]}")
        print(separador(33, 3))
        mudanca = input("Se todas informações estiverem corretas digite 0\nSe não digite o número que deseja mudar: ")

def simulacaoVistoria():
    clear_console()
    print(separador(33, 2))
    bike_dano = input("A bike possui algum dano que afete o funcionamento? [S/N] ").strip().upper()
    bike_dano = validacao(bike_dano, 5, var="")
    if bike_dano[0] == "S":
        dano = input("Informe o dano existente na bike: ")

    bike_dano_estetico = input("A bike possui algum dano estético? [S/N] ").replace(" ", "").upper()
    bike_dano_estetico = validacao(bike_dano_estetico, 6, var="")

    if bike_dano_estetico[0] == "S":
        dano = input("Informe o dano existente na bike: ")
        print("O seguro da bike foi aprovado, porém não cobriremos esse dano!")
        print(separador(33, 2))
            
    elif bike_dano_estetico[0] == "N":
        print("Seguro da bike foi aprovado!")
        print(separador(33, 2))


def addLista(lista, *var):
    for c in var:
        lista.append(c)

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

def validaValor():
    while True:
        valor = input("Valor da bike: R$").strip().replace(",", ".")
        try:
            valor_float = float(valor)
            return valor_float
        except ValueError:
            print(separador("Digite um valor válido.", 6))

def validarNserie(n_serie):
    while len(n_serie) != 11:
        clear_console()
        print(separador(33, 3))
        print(separador("Opção inválida!", 6))
        n_serie = input("Número de série (11 caracteres): ")
    return n_serie


def principal():
    option = ""
    clear_console()
    print(separador(33, 2))
    while option != "6":
        option = input("1- Fazer seguro de bike\n2- Saber sobre o seguro de bike\n3- Termos de privacidade e segurança3\n6- Sair\n")
        option = validacao(option, 4, var="")
        if option == "1":
            cadastroCliente()
            bike()
            simulacaoVistoria()

        elif option == "2":
            clear_console()
            print(separador(33, 2))
            print("Bem-vindo ao nosso Seguro de Bicicleta, uma maneira simples e segura de proteger sua bicicleta contra imprevistos. Na Porto Seguro, compreendemos o valor que sua bicicleta tem para você, seja para o lazer ou para deslocamentos diários. Com nosso seguro de bicicleta, você pode pedalar com tranquilidade, sabendo que está protegido.\n\nPor que escolher o Seguro de Bicicleta da Porto Seguro:\n\n- Cobertura Abrangente: Nosso seguro oferece cobertura contra roubo, furto qualificado e danos acidentais à sua bicicleta.\n- Ampla Rede de Oficinas Parceiras: Trabalhamos com uma ampla rede de oficinas especializadas para garantir o melhor atendimento em caso de reparos.\n- Cobertura em Todo o Brasil: Esteja você pedalando na cidade ou explorando trilhas, nosso seguro oferece cobertura em todo o território nacional.\n- Facilidade de Contratação: Você pode adquirir seu seguro de bicicleta de forma rápida e descomplicada, diretamente pelo aplicativo.")
            print(separador(33, 2))

        elif option == "3":
            clear_console()
            print(separador(33, 4))
            url = "https://www.portoseguro.com.br/conteudo/mobile/portoseguro/politica-de-privacidade.html"
            webbrowser.open(url)


        elif option == "4":
            clear_console()
            print(separador(33, 4))
            

    
    



#Programa principal
principal()