
def binomial(n, m):
    # condizione terminale
    if m == 0 or n == m:
        return 1
    # condizione non terminale
    else:
        return binomial(n-1, m-1) + binomial(n-1, m)

if __name__ == '__main__':
    N = 5
    M = 3
    print(binomial(N, M))