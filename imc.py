# Calculo IMC
#1 capturar as infos de peso e altura
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

#2 calcular o imc 
imc = peso / (altura ** 2)

#3 classificar o IMC 
if imc < 18.5:
    print(f'Baixo peso - IMC: {imc:.2f}')
elif imc < 24.9:
    print(f'Peso normal - IMC: {imc:.2f}')
elif imc < 29.9:
    print(f'Pré Obsesidade - IMC: {imc:.2f}')
elif imc < 34.9:
    print(f'Obesidade Grau 1 - IMC: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade Grau 2 - IMC: {imc:.2f}')
else:
    print(f'Obesidade Grau 3 - IMC: {imc:.2f}')



