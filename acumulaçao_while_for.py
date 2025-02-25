#lista de compras

lista_de_compras = [
    ('Camiseta', 19.90),
    ('Calça Jeans', 20.50),
    ('Meia G', 5.90)
]

#Encontrar a forma de percorrer toda a lista e somar os valores

#Problema: qUal é o total desse carrinho de compras ?

#tupla[0] >> nome do item
#tupla[1] >> preço

#variavel de controle
indice = 0
#variavel para adicionar a soma
total_de_compras = 0

#usando while 

# percorre cada item da lista e enquanto o indice for menor que o tamnho de lista continua percorrendo e armazene na variavel total
while indice < len(lista_de_compras): 
   total_de_compras += lista_de_compras[indice][1] #acessa o valor do preço e acumula na variavel total de compra
   indice +=1 #sempre atualize o valor do controle e some +1 para ir para o proximo valor (item) e somar,  até chegar no final do tamanho da lista
   
print(f' O total de compras do seu carrinho : {total_de_compras}')

#continua com for

print(f'resolução com for')

total = 0

for compra in lista_de_compras:
    total += compra[1]

#interaçao 1 compra = lista_de_compras[0]
# total += compra[1]
#interação 2 compra = lista_de_compras[1]
# total += compra[1]

#cada elemento da lista ele acumula o valor na posição 1

print(f'Total de compras com o for: {total}')
