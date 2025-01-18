# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

# Funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamado função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado:", resultado_quadrado)

# Funcao com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamado a função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(20, 50)
print("A soma do numero %s e o número %s é %s" % (numero1, numero2, resultado_soma))
