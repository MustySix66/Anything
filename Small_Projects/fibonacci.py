def fibonacci(n):
    # 2 first numbers from fibonacci's
    secuencia = [0, 1]
    # Generate next numbers un the sequence.
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

# Example
num=int(input("How many number u wanna see? "))
print(fibonacci(num))  # Imprime los primeros 10 números de la secuencia de Fibonacci