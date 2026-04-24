
# restituisce True o False
# si potrebbe fare in modo iterativo senza usare la ricorsione e non sarebbe troppo lungo
def dichotomic(input_list, val):
    # caso terminale
    if len(input_list) == 1:            # se la lunghezza della lista è 1
        if input_list[0] == val:        # se il valore che cerco è nella prima posizione della lista
            return True                 # ritorno vero
        else:
            return False                # altrimenti ritorno falso
    # caso ricorsivo
    else:
        index = len(input_list)//2    # trovo indice a metà
        return (dichotomic(input_list[:index], val)     # se val è contenuto nella prima parte della sequenza
                or dichotomic(input_list[index:], val)) # se val è contenuto nella seconda parte della sequenza

if __name__ == '__main__':
    sequenza = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    print(dichotomic(sequenza, 4))          # restituisce True perchè è contenuto nella sequenza
    print(dichotomic(sequenza, 11))         # restutuisce False perchè non è contenuto nella sequenza