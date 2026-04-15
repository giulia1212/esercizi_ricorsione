
# devo scorrere ogni singolo elemento e se vedo una stringa devo fare +1,
# se è una lista devo fare la ricorsione
# condizione terminale: se la lista è vuota ritorno zero
# in questa funzione non ha fatto nessun controllo per l'input
# all'esame devi fare tutti i controlli per evitare ogni tipo di problema

# se vuoi vedere la versione iterativa senza la ricorsione la trovi
# alla slide 34 delle slide sulla ricorsione, è più lunga
def count_leaf_nodes(input_list):
    # terminale
    if len(input_list) == 0:
        return 0
    # non terminale
    else:
        counter = 0
        for element in input_list:
            # check if element is a list
            # if it is a list, we count its element with a recursion
            if type(element) == list:
                counter += count_leaf_nodes(element)
            # else, we add +1
            else:
                counter += 1
    return counter


if __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) # ci aspettiamo 10 come risultato in questo caso

