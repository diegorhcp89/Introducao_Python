# Criando um dicionário de exemplo
pessoa = {"nome": "Diego", "idade": 38, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valroes por chave
print("Nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Amaral"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 39
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Métoso values
valores = list(pessoa.values())
print("Valores do dicionários:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor: %s = %s" % (itens[0][0], itens[0][1]))