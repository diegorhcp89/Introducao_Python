# Declaração
nome_completo = "Diego F do Amaral"

nome_completo_aspas = """Diego
Amaral"""

nome_completo_quebra= "Diego \
    Amaral"

nome = "Diego"
sobrenome = "Amaral"


#Formatação
print("Nome complete (1a forma):", nome_completo)
print("Nome complete (2a forma):" +  nome_completo)
print("Nome complete (3a forma):" + " Diego" + " Amaral")
print("Nome complete (4a forma):" + " Diego" , " Amaral")
print("Nome complete (5a forma):", nome_completo_aspas)
print("Nome complete (6a forma):",nome_completo_quebra)
print("Nome complete (7a forma): %s" % nome_completo)
print("Nome complete (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome complete (9a forma): {nome} {sobrenome}")
print("Nome complete (10a forma): {} {}".format(nome, sobrenome))
