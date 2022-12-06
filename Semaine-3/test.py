# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# fib(2000)

def initialisation():
    
    symbols = ["A", "J", "Q", "R"]
    temp_1 = symbols[:1]
    temp_2 = [str(i) for i in range(2,11)]
    temp_3 = symbols[1:]

    # temp_4 = []
    # for i in range(2,11):
    #     temp_4.append(str(i))

    SYMBOLS = tuple(temp_1 + temp_2 + temp_3)
    SUITS = ("♦", "♣", "♥", "♠")

    paquet = []
    for suit in SUITS:
        for symbol in SYMBOLS:
            paquet.append(f"{symbol}{suit}")

    return paquet

initialisation()