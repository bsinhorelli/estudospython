def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: O cpf deve conter apenas números'
    if len(cpf) != 11:
        return 'Erro: O cpf deve ter exatamente 11 dígitos.'
    return 'cpf válido.'
    
cpf = input('Digite seu cpf: ')
print(validar_cpf(cpf))
