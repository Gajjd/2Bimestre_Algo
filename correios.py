pacotes = ( ("ABC123","Enviado"), ("XYZ", "Recebido"), ("DEF", "Em Trânsito"), ("JKL321", "Enviado"), ("MNO654", "Recebido"), ("PQR987", "Em Trânsito"), ("STU741","Enviado") ) 

# 1 Quantos pacotes com status "Enviado", "Recebido" e "Em trânsito"

contagem = {"Enviado": 0, "Recebido": 0, "Em Trânsito": 0}
for codigo, status in pacotes:
    if status in contagem:
        contagem[status] += 1

print(contagem)


# 2 Listar apenas os códigos com status "Em trânsito"

statusEmTransito = []
def listarEmTransito(pacotes):
    global statusEmTransito
    for codigo, status in pacotes:
        if status == "Em trânsito":
            statusEmTransito.append(codigo)
    return statusEmTransito

print(listarEmTransito(pacotes))
print(statusEmTransito)

# 3 Função para receber um código de rastreamento e retornar o status do pacote ou uma mensagem informando que o pacote não está cadastrado


# 4 Ordenar os pacotes pelo código de rastreamento e exibir tupla ordenada. Desenvolva um programa que execute essas operações e exiba os resultados, explicando o metodo de implementação