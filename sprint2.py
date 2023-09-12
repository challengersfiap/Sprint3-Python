import random

def validacao_option(o):
    while o != "1" and o != "2" and o != "3":
        print("-=" * 25)
        o = input("Opção inválida! Selecione novamente!\n1- Fazer seguro da bike\n2- Saber informação sobre seguro de bike\n3- Sair\n")
        print("-=" * 25)
    return o

def info_correta(i, nome, cpf, modelo, cor, nserie):
    print('-='*25)
    mensagem = "Nome: {}\nCPF: {}\nModelo: {}\nCor: {}\nNúmero de série: {}".format(nome, cpf, modelo, cor, nserie)
    print(mensagem)
    i = input("As informações estão corretas agora? [S/N] ").replace(" ","").upper()
    while i != "S" and i != "N":
        i = input("Opção inválida\nAs informações estão corretas agora? [S/N] ").replace(" ", "").upper()
    return i

def validacao_mudanca():
    print("-=" *25)
    m = input("Qual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "")
    print("-=" *25)
    while m != "1" and m != "2" and m != "3" and m != "4" and m != "5":
        print("-=" *25)
        m = input("Opção inválida!\nQual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "").upper()
        print("-=" *25)
    return m


repete = 0

print("-="*25)
option = input("1- Fazer seguro da bike\n2- Saber informação sobre seguro de bike\n3- Sair\n")
print("-="*25)

if option != "1" and option != "2" and option != "3":
    option = validacao_option(option)

#while com a condição da variavel "repete", para caso o usuário queira tentar novamente se o seguro não for aprovado
while repete == 0:
    if option == "1":
        #Captando dados do cliente como nome e CPF
        cliente_nome = input("Digite seu nome completo: ")
        cliente_cpf = input("Informe o seu CPF: ")
        print("-="*25)
        print("Para continuar a vistoria, você deve estar próximo a bike!")

        #Captando dados da bike do cliente
        bike_modelo = input("Informe o modelo da bike: ")
        bike_cor = input("Informe a cor da bike: ")
        bike_nserie = input("Digite o número de série da bike: ")
        print("-="*25)

        #mostrando os dados que o cliente preencheu e em seguida perguntando se deseja alterar alguma coisa
        print(f"Verifique se as informações estão corretas:\nNome: {cliente_nome}\nCPF: {cliente_cpf}\nModelo: {bike_modelo}\nCor: {bike_cor}\nNúmero de série: {bike_nserie}")
        correto = input("Todas informações estão corretas? [S/N] ").replace(" ", "").upper()

        while correto != "S" and correto != "N":
            correto = input("Opção inválida!\nTodas as informações estão corretas? [S/N] ").replace(" ", "").upper()
        
        if correto == "S":
            print("-="*25)

        #pedindo o campo que o cliente deseja alterar
        elif correto == "N":
            mudanca = validacao_mudanca()
            
            #laço de repetição cujo utilidade seja para o cliente alterar os dados quantas vezes quiser
            while correto == "N":
                if mudanca == "1":
                    print('-='*25)
                    cliente_nome = input("Nome: ")
                    correto = info_correta(correto, cliente_nome, cliente_cpf, bike_modelo, bike_cor, bike_nserie)

                    if correto == "N":
                        print('-='*25)
                        mudanca = input("Qual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "")
                        print('-='*25)

                elif mudanca == "2":
                    cliente_cpf = input("CPF: ")
                    correto = info_correta(correto, cliente_nome, cliente_cpf, bike_modelo, bike_cor, bike_nserie)

                    if correto == "N":
                        print('-='*25)
                        mudanca = input("Qual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "")
                        print('-='*25)

                elif mudanca == "3":
                    print('-='*25)
                    bike_modelo = input("Modelo:")
                    correto = info_correta(correto, cliente_nome, cliente_cpf, bike_modelo, bike_cor, bike_nserie)

                    if correto == "N":
                        print('-='*25)
                        mudanca = input("Qual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "")
                        print('-='*25)

                elif mudanca == "4":
                    print('-='*25)
                    bike_cor = ("Cor: ")
                    correto = info_correta(correto, cliente_nome, cliente_cpf, bike_modelo, bike_cor, bike_nserie)

                    if correto == "N":
                        print('-='*25)
                        mudanca = input("Qual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "")
                        print('-='*25)

                else:
                    print('-='*25)
                    bike_nserie = input("Número de série: ")
                    correto = info_correta(correto, cliente_nome, cliente_cpf, bike_modelo, bike_cor, bike_nserie)

                    if correto == "N":
                        print('-='*25)
                        mudanca = input("Opção inválida!\nQual informação deseja mudar:\n1-Nome\n2-CPF\n3-Modelo:\n4-Cor:\n5-Número de série\n").replace(" ", "")
                        print('-='*25)



        bike_dano = input("A bike possui algum dano que afete o funcionamento? [S/N] ").replace(" ", "").upper()#"Transformando" a variavel em maiuscula para evitar erro na hora do if ↓↓

        while bike_dano != "S" and bike_dano != "N":
            bike_dano = input("Opção inválida!\nA bike possui algum dano que afete o funcionamento? [S/N] ").upper().replace(" ", "")

        #condição para caso haja dano na bike
        if bike_dano[0] == "S":
            dano = input("Informe o dano existente na bike: ") #Uma variavel sem utilidade para o nível que estamos na matéria(a intenção é conseguirmos ler  mensagem e o programa interpretar a mensageme, e dizer se a bike está aprovada ou não)

            #↓↓ a utilidade é para "interpretar" o dano que a bike possui, e o sistema analisar se o seguro é aprovado ou não
            if bike_dano[0] == "S":
                dano = input("Informe o dano existente na bike: ")

        #↓↓ Na parte de dano estético não fiz o randint por conta que a porto não cobre danos estéticos, apenas funcionais
        bike_dano_estetico = input("A bike possui algum dano estético? [S/N] ").replace(" ", "").upper()

        while bike_dano_estetico != "S" and bike_dano_estetico != "N":
            print("Opção inválida!")
            bike_dano_estetico = input("A bike possui algum dano estético?[S/N] ").replace(" ", "").upper()

        #condição para informar se existente, o dano da bicicleta
        if bike_dano_estetico[0] == "S":
            dano = input("Informe o dano existente na bike: ")
            print("O seguro da bike foi aprovado, porém não cobriremos esse dano!")
            print("-="*25)
            break

        elif bike_dano_estetico[0] == "N":
            print("Seguro da bike foi aprovado!")
            print("-="*25)
            break

    #Caso o cliente queira apenas saber sobre o seguro e caso ele queira fazer o seguro digita: "1"
    elif option == "2":
        print("Nosso seguro de bike...")
        option = input("Digite 1 caso queira fazer nosso seguro, caso contrário 0: ").replace(" ", "")
        print("-="*25)
        if option == "0":
            break
    
    elif option == "3":
        print("Agradecemos por entrar em contato! A qualquer momento estamos a disposição!")
        print("-="*25)
        break