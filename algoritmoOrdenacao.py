lista = [1, 3, 5, 6, 7, 0, 2, 4, 6, 8]

# listaOrdenada = sorted(lista)
# print(listaOrdenada)

# # Ou

# print(sorted(lista))

# # Ou

# for i in range(len(lista)):
#     for j in range(len(lista) - 1):
#         if lista[j] > lista[j + 1]:
#             troca = lista[j]
#             lista[j] = lista[j+1]
#             lista[j+1] = troca
            
# print(lista)

# Ou

for i in range(len(lista)):
    maior = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[maior]:
            maior = j
            
    troca = lista[i]
    lista[i] = lista[maior]
    lista[maior] = troca

print(lista)

