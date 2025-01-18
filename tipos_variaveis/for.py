print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
lista = (1, 2, 3, 4, 5)
for elemento in lista:
    print(elemento)

pessoa = {"nome": "Diego", "idade":38, "cidade": "São Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando dicionario - Items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")