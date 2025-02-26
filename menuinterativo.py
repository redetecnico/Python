while True :
    op = input('Digite a opção desejada:\n1- Saudação\n2- Sair\n3- Nenhuma da alternativas\n')
    if op == '1':
       print ('uma saudação qualquer')
    elif op == '2':
        break #interrompe o loop e vai até a ultima opçao no caso print(fim)
    elif op == '3':
        continue
    else:
       print('Opção invalida')

print ('fim')

