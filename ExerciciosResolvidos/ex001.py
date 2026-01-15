valor = float(input('Digite o valor de sua conta: '))
porcentagem = float(input('Digite a porcentagem da gorjeta: '))
gorjeta = (porcentagem/100) * valor
total = valor + gorjeta
print(f'Valor total da gorjeta é R$ {gorjeta:.2f}')
print(f'Total da conta é R$ {total:.2f}')
