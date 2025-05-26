lista = []
item = ""
opcao = ""
removeu = False

while opcao != "f":
    opcao = input("Deseja adicionar um item a lista? (s para sim) (n para não) (f para finalizar): ").lower()
    if opcao == "s":
        item = input("Digite o nome do item: ")
        lista.append(item)
        
    elif opcao == "n":
        if len(lista) != 0:
            while removeu == False:
                item = input("Digite o nome do item a ser removido exatamente como está na lista: ")
                for i in lista:
                    if item == i:
                        lista.remove(item)
                        removeu = True
                if removeu == False:
                    print("Verifique as acentuações, maiúsculas e minúsculas")
            removeu = False
        else:
            print("A lista ainda não possui um item.")
    elif opcao == "f":
        print("A lista ficou assim:")
        print(lista)
        