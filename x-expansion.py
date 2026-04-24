import copy


# come risultato dovrebbe darmi una lista con tutte le stringhe che sono soluzione
# si dovrebbero anche fare tutti i vari controlli che le lettere siano maiuscole ecc.
# ma qua non lo facciamo, all'esame devi fare tutti i controlli
class XExpansion:
    def __init__(self):
        self.soluzioni = []
        self.soluzioni_list = []

    # calcola_list fa la stessa cosa di calcola ma interpreta parziale come una lista invece che come una stringa
    def calcola_list(self, input):
        self.soluzioni = []
        self._ricorsione_list([], input)

    def _ricorsione_list(self, parziale: list, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            self.soluzioni_list.append(copy.deepcopy(parziale))  # copio soluzione parziale nella lista delle soluzioni
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                # ciclare sugli step possibili
                for c in ["0", "1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()
            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])

    def calcola(self, input):
        self.soluzioni = []    # devi mettere di nuovo a zero le soluzioni
                               # altrimenti se scrivi due volte le istruzioni "prova" ti appende
                               # le soluzioni nuove alle soluzioni di prima
        self._ricorsione("", input)

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    # esamino un carattere per volta, se è X devo fare una versione con 0 e una con 1
    def _ricorsione(self, parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            self.soluzioni.append(parziale) # aggiungo soluzione parziale alla lista delle soluzioni
        #caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                self._ricorsione(parziale+'0', rimanenti[1:])
                self._ricorsione(parziale+'1', rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# si può anche fare senza usare una classe
def x_expansion2(input):
    soluzioni = []
    def ricorsione(parziale: str, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            soluzioni.append(parziale)
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                ricorsione(parziale+'0', rimanenti[1:])
                ricorsione(parziale+'1', rimanenti[1:])
            else:
                ricorsione(parziale+rimanenti[0], rimanenti[1:])
    ricorsione("", input)
    return soluzioni




if __name__ == '__main__':
    sequenza = "01X0X"
    xexp = XExpansion()

    # metodo con soluzioni parziali rappresentate come stringhe
    xexp.calcola(sequenza)                                      # "prova"
    print(xexp.soluzioni)   # stampa la lista delle soluzioni   # "prova"

    # metodo con soluzioni parziali rappresentate come liste
    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)

    # senza usare la classe
    print(x_expansion2(sequenza))

