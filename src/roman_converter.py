def roman_to_decimal(roman):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    anterior = 0

    for letra in reversed(roman):
        valor = valores[letra]
        if valor < anterior:
            resultado -= valor
        else:
            resultado += valor
        anterior = valor

    return resultado

