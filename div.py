def verificar_divisibilidade(numero):
    divisibilidade = {}
    for divisor in range(2, 13):
        divisibilidade[divisor] = numero % divisor == 0
    return divisibilidade

def main():
    numero = int(input("Digite um número inteiro positivo: "))

    resultado = verificar_divisibilidade(numero)

    print(f"Divisibilidade de {numero}:")
    for divisor, divisivel in resultado.items():
        print(f"É divisível por {divisor}: {divisivel}")

if __name__ == "__main__":
    main()
