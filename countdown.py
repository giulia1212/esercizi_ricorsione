from time import sleep

# funzione iterativa
def countdown(n):
    while n >= 0:
        print(n)
        #sleep(1)    # fa una pausa di un secondo
        n -= 1

# funzione RICORSIVA
def countdown_recursive(n):
    # devi sempre prima controllare l'input, qui dovresti controllare anche che sia intero oltre che negativo
    if n < 0:
        print("Sorry, negative")
        return
    # condizione terminale, IMPORTANTE altrimenti va all'infinito
    if n == 0:
        print("Stop")
    # condizione non terminale
    else:
        print(n)
        #sleep(1)
        countdown_recursive(n-1)


if __name__ == '__main__':
    N = 4
    countdown(N)
    countdown_recursive(N)
