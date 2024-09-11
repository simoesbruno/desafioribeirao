def contar_letras_a(string):
    contagem = string.lower().count('a')
    
    if contagem > 0:
        return f"A letra 'a' ocorre {contagem} vez(es) na string."
    else:
        return "A letra 'a' não foi encontrada na string."
string = input("Informe uma string: ")
print(contar_letras_a(string))
