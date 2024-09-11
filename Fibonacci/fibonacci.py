def is_fibonacci(n):
    def generate_fibonacci(limit):
        fib_sequence = [0, 1]
        while fib_sequence[-1] < limit:
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)
        return fib_sequence

    fib_sequence = generate_fibonacci(n)

    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(is_fibonacci(numero))