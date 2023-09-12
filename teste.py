import datetime

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

print(separador(16, 1))

atual = datetime.date.today()
print(atual)
print(atual.year)
print(atual.strftime("%A"))

print("\x1b[32mTexto em verde\x1b[0m")

valor = 12345.67
valor_formatado = f"${valor:,.2f}"
print(valor_formatado)

minha_lista = []

var1 = "valor1"
var2 = 42
var3 = ["a", "b", "c"]

minha_lista.extend([var1, var2, var3])
# ou
minha_lista += [var1, var2, var3]

print(minha_lista)