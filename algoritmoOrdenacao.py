lista = [1, 3, 5, 6, 7, 0, 2, 4, 6, 8]

# # Jeitos de fazer a lista ficar ordenada:

# # 1:
# listaOrdenada = sorted(lista)
# print(listaOrdenada)
#________________________________________

# # 2:
# print(sorted(lista))
#________________________________________

# # 3:
# for i in range(len(lista)):
#     for j in range(len(lista) - 1):
#         if lista[j] > lista[j + 1]:
#             troca = lista[j]
#             lista[j] = lista[j+1]
#             lista[j+1] = troca
            
# print(lista)
#________________________________________

# 4:
# for i in range(len(lista) - 1, 0, -1):
#     maiorIndice = 0
#     for j in range (1, i + 1):
#         if lista[j] > lista[maiorIndice]:
#             maiorIndice = j
#     troca = lista[i]
#     lista[i] = lista[maiorIndice]
#     lista[maiorIndice] = troca

#     print(lista)

# print(f"Lista ordenada: {lista}")
#________________________________________
