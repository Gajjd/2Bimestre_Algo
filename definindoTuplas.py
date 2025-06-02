numero = (5, 6, 12, 8, 7, 8, 3,)
# # Para definir uma tupla, usa-se os parenteses

# print(f"Tupla original: {numero}")
# # Imprimindo para o usuario a tupla original, sem manipulações

# print(f"Tamanho da tupla: {len(numero)}")
# # Não é necessário usar dois parenteses

# print("Acessando pelo índice",numero[2])
# # Escolhendo qual numero sera mostrado atraves do indice, lembrando que começa do zero

# print(f"Fazendo um slicing do 2 ao 5 {numero[2:5]}")
# # O slicing não pega o ultimo item definiso no recorte

# print(f"Quantas vezes o número 8 repete: {numero.count(8)} vezes")
# # tupla.count(ITEM) conta quantas vezes o ITEM foi reptido

# print(f"Posição da primteira ocorrencia do número 7: {numero.index(7)}")
# # tupla.index(ITEM) mostra o indice da primeira aparição do ITEM

# minimoTupla = min(numero)
# print(minimoTupla)
# print(f"O menor número da tupla numero: {min(numero)}")
# # min(TUPLA) mostra o menor item da TUPLA

# maximoTupla = max(numero)
# print(maximoTupla)
# print(f"O maior número da tupla numero: {max(numero)}")
# # max(TUPLA) mostra o maior item da TUPLA

# somaTupla = sum(numero)
# print(somaTupla)
# print(f"A soma dos números da tupla numero: {sum(numero)}")
# # sum(TUPLA) mostra a soma dos itens da TUPLA

# tuplaOrdenada = sorted(numero)
# print(tuplaOrdenada)
# print(f"Tupla organizada do menor ao maior: {sorted(numero)}")
# # sorted(TUPLA) mostra os itens da TUPLA organizados de forma crescente

# print(f"O número 4 está na tupla? {4 in numero}")
# # Quando usamos o "in", verificaremos os espaços na lista, retornando True para verdadeiro e False para falso

numero2 = (15, 20)
tuplaConcatenada = numero + numero2
print(f"A concatenação das tuplas numero e numero2 resulta na nova tupla: {tuplaConcatenada}")

numeroAoQuadrado = []
for i in numero:
    numeroAoQuadrado.append(i*2)
    
print(numeroAoQuadrado)