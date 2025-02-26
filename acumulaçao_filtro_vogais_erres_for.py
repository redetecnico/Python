#Contar quantas vogais uma frase possui


texto = 'o rato roeu a roupa do rei de roma'

#quantas vezes aparecem vogais no texto ?

vogal = 0 

for caractere in texto:
    if caractere.lower() in 'aeiou':
        vogal +=1

print('Total de vogais: {}'.format(vogal))

#numero de erres

erres = 0

for caractere in texto:
   if 'r' in caractere.lower():
      erres +=1 

print('Total de erres: {}'.format(erres))
       