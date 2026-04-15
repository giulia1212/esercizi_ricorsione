
# usando RICORSIONE
def palyndrome(word):
    # terminale
    if len(word) <= 1:
        return True
    # non terminale
    else:
        return word[0] == word[-1] and palyndrome(word[1:-1])

# senza u
# sare ricorsione, questo è possibile però solo grazie a quello che hanno
# già implementato gli sviluppatori di python per semplificare alcune operazioni
def palyndrome_banale(word):
    return word[::-1] == word    # word[::-1] mi da la parola al contrario


if __name__ == '__main__':
    print(palyndrome('casa'))
    print(palyndrome('civic'))

    print(palyndrome_banale('casa'))
    print(palyndrome_banale('civic'))