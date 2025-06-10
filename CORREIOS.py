codigosPacotes = ["ABC123", "XYZ789", "DEF456", "JKL321", "MNO654", "PQR987", "STU741"]
statusPacotes = ["Enviado", "Recebido", "Em Trânsito", "Enviado", "Recebido", "Em Trânsito", "Enviado"]

# 1 Quantos pacotes com status "Enviado", "Recebido" e "Em trânsito"

print("Quantidade de pacotes por status:")

quantidadeEnviados = statusPacotes.count("Enviado")
quantidadeRecebidos = statusPacotes.count("Recebido")
quantidadeEmTransito = statusPacotes.count("Em Trânsito")

print(f"Enviado: {quantidadeEnviados}")
print(f"Recebido: {quantidadeRecebidos}")
print(f"Em Trânsito: {quantidadeEmTransito}")

print("___________________________________________")

# 2 Listar apenas os códigos com status "Em trânsito"

print("Códigos dos pacotes com status Em Trânsito:")

def CodigosEmTransito():
    resultado = []
    for i in range(len(codigosPacotes)):
        if statusPacotes[i] == "Em Trânsito":
            resultado.append(codigosPacotes[i])
    return resultado

codigosEmTransito = CodigosEmTransito()
print(f"{codigosEmTransito}")

print("___________________________________________")

# 3 Função para receber um código de rastreamento e retornar o status do pacote ou uma mensagem informando que o pacote não está cadastrado

print("Consultar status do pacote pelo código:")

def consultarStatus(codigo):
    if codigo in codigosPacotes:
        indice = codigosPacotes.index(codigo)
        return f"Status de {codigo}: {statusPacotes[indice]}"
    else:
        return f"Pacote {codigo} não está cadastrado."


print(consultarStatus("DEF456"))
print(consultarStatus("XXX123"))

print("___________________________________________")

# 4 Ordenar os pacotes pelo código de rastreamento e exibir tupla ordenada. Desenvolva um programa que execute essas operações e exiba os resultados, explicando o metodo de implementação

print("Lista de pacotes ordenada pelo código:")

listaPacotes = []
for i in range(len(codigosPacotes)): # Eu usei o range para nao ficar com um a menos
    listaPacotes.append((codigosPacotes[i], statusPacotes[i])) # Aqui eu juntei as duas listas em uma só, que nem estava antes

listaOrdenada = sorted(listaPacotes) # Como o codigo vem antes do status, eu pude usar o sorted para ordenar

for pacote in listaOrdenada:
    print(f"{pacote}")
