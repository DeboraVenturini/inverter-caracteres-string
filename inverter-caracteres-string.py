def inverte_string(string):
    tamanho = len(string)
    string_invertida = ''
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string_original = input("Digite a string que deseja inverter: ")

string_invertida = inverte_string(string_original)
print("String invertida:", string_invertida)
