loop = 1
while loop == 1:
    print("___________________________________________")
    sacar = input("Digite o montante a sacar...")
    if (sacar.isdigit()):
        saque = float(sacar)
    print("___________________________________________")
    metodo = int(input("Digite o metodo [1] Pix [2] Maquininha de Cartao ...."))

    if metodo == 1:
        total = saque + (saque * 0.1)
        print("Total a sacar: {}".format(total))
        continuar = input("Digite [Y] para continuar ou [N] para sair...")
        continuar = continuar.upper()
        if continuar == 'Y':
            continue
        elif continuar == 'N':
            loop = 0
        else:
            input("Caractere invalido * {} * nao declarado no escopo...")
            continue
    elif metodo == 2:
        total = saque + (saque * 0.3)
        print("Total a sacar: {}".format(total))
        continuar = input("Digite [Y] para continuar ou [N] para sair...")
        continuar = continuar.upper()
        if continuar == 'Y':
            continue
        elif continuar == 'N':
            loop = 0
        else:
            input("Caractere invalido * {} * nao declarado no escopo...")
            continue
    elif metodo == 3:
        taxa = int(input("Digite a taxa para sacar..."))
        total = saque + (saque * (taxa / 100))
        print("Total a sacar: {}".format(total))
        continuar = input("Digite [Y] para continuar ou [N] para sair...")
        continuar = continuar.upper()
        if continuar == 'Y':
            continue
        elif continuar == 'N':
            loop = 0
        else:
            input("Caractere invalido * {} * nao declarado no escopo...")
            continue
    else:
        print("Digite um metodo disponivel * {} * nao declarado no escopo".format(metodo))
        continue
