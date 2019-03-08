def digito(peso, fim):
    s = 0
    i = 0
    while i < fim:
        valor = int(cpf(i)) * peso
        s += valor
        peso = peso - 1
        i += 1
    d1 = s * 10 % 11
    if d1 == 10 or d1 == 11:
        d1 = 0
    return d1
cpf = "123.456.789-01"
cpf = cpf.replace(".", " ")
cpf = cpf.replace("-", " ")
if len(cpf) == 11:
    d1 = digito(10, 9)
    d2 = digito(11, 10)
    print(d1, d2)
    if d1 == int(cpf[9]) and d2 == int(cpf[10]):
        print("Válido")
    else:
        print("Inválido")
