# Rodizio SP
#1 Capturar o numero da placa
mensagem = 'Saiba se seu carro está no rodízio'
placa = int(input('Digite o final de sua placa: '))
dia = str (input('Digita o dia da semana:'))

#2 Validar se seu carro está no Rodizio  
  
if dia == 'segunda' and placa == 2:
    print ('Você está no rodizio')
elif dia == 'segunda' and placa == 1:
    print ('Você está no rodizio')
elif dia == 'segunda' and placa == 0:
    print ('Você não está no rodizio')
elif dia == 'segunda' and placa > 2:
    print ('Você não está no rodizio')
elif dia == 'terça' and placa == 3:
    print ('Você está no rodizio')
elif dia == 'terça' and placa == 4:
    print ('Você está no rodizio')
elif dia == 'terça' and placa == 0:
    print ('Você não está no rodizio')
elif dia == 'terça' and placa > 4:
    print ('Você não está no rodizio')
elif dia == 'quarta' and placa == 5:
    print ('Você está no rodizio')
elif dia == 'quarta' and placa == 6:
    print ('Você está no rodizio')
elif dia == 'quarta' and placa == 0:
    print ('Você não está no rodizio')
elif dia == 'quarta' and placa > 6:
    print ('Você não está no rodizio')
elif dia == 'quinta' and placa == 7:
    print ('Você está no rodizio')
elif dia == 'quinta' and placa == 8:
    print ('Você está no rodizio')
elif dia == 'quinta' and placa == 0:
    print ('Você não está no rodizio')
elif dia == 'quinta' and placa > 8:
    print ('Você não está no rodizio')
elif dia == 'sexta' and placa == 9:
    print ('Você está no rodizio')
elif dia == 'sexta' and placa == 0:
    print ('Você está no rodizio')
elif dia == 'sexta' and placa <9:
    print ('Você não está no rodizio')







