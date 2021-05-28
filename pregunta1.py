# Implementa la función fib(n) que retorna el n-ésimo número de la serie
# de Fibonacci:
# fib(1) = 1
# fib(2) = 1
# fib(n) = fib(n - 1) + fib(n - 2), para todo n > 2.


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # Prueba de la función: imprime los primeros 10 números en una línea
    # separados por coma y espacio.
    prueba_fib = ''
    for i in range(10):
        prueba_fib+=str(fib(i))+" , "
    prueba_fib=prueba_fib[:-2]
    print(prueba_fib)
