'''
Scrivi un metodo ricorsivo che restituisce True se ci sono esattamente tre numeri dispari nella 
lista e la loro somma è minore del primo elemento della lista.
'''
def verifica(self):
    if self._testa is None:
        return False
    return self._verifica_da(self._testa, 0, 0, self._testa.info)

def _verifica_da(self, nodo, count, somma, primo):
    if nodo is None:
        return count == 3 and somma < primo
    if nodo.info % 2 == 1:
        count += 1
        somma += nodo.info
    return self._verifica_da(nodo.successivo, count, somma, primo)

'''
Scrivere un metodo verifica() che restituisce True se e solo se:
• tutti gli elementi in posizione pari (0, 2, 4, …) sono pari
• tutti gli elementi in posizione dispari (1, 3, 5, …) sono dispari
'''
def verifica(self):
    if self._testa is None:
        return False
    return self._verifica_da(self._testa, 0)

def _verifica_da(self, nodo, posizione):
    if nodo is None:
        return True
    if posizione % 2 == 0 and nodo.info % 2 == 1:
        return False
    if posizione % 2 == 1 and nodo.info % 2 == 0:
        return False
    return self._verifica_da(nodo.successivo, posizione + 1)

'''
Scrivere un metodo verifica(self) che restituisce True se e solo se:
Tutti i numeri pari della lista compaiono prima di tutti i numeri dispari.
'''
def verifica(self):
    return self._verifica_da(self._testa, False)

def _verifica_da(self, nodo, trovato_dispari):
    if nodo is None:
        return True
    if nodo.info % 2 == 1:
        trovato_dispari = True
    elif trovato_dispari and nodo.info % 2 == 0:
        return False
    return self._verifica_da(nodo.successivo, trovato_dispari)

'''
Scrivere un metodo verifica(self) che restituisce True se e solo se 
la lista contiene almeno due numeri consecutivi (cioè due nodi successivi con valori che differiscono di 1, come 7 e 8, o 12 e 11).
'''
def verifica(self):
    return self._verifica_da(self._testa)

def _verifica_da(self, nodo):
    if nodo is None or nodo.successivo is None:
        return False
    if abs(nodo.info - nodo.successivo.info) == 1:
        return True
    return self._verifica_da(nodo.successivo)

'''
Scrivere un metodo verifica(self) che restituisce True se e solo se la lista contiene almeno due numeri pari consecutivi, 
ma non contiene tre dispari consecutivi.
'''
def verifica(self):
    return self._verifica_da(self._testa, False, 0)

def _verifica_da(self, nodo, trovato_pari_consecutivi, count_dispari):
    if nodo is None or nodo.successivo is None:
        # ritorna True solo se è stato trovato almeno una coppia di pari consecutivi
        return trovato_pari_consecutivi
    # Verifica due pari consecutivi
    if nodo.info % 2 == 0 and nodo.successivo.info % 2 == 0:
        trovato_pari_consecutivi = True
    # Aggiorna contatore dispari consecutivi
    if nodo.info % 2 == 1:
        count_dispari += 1
        if count_dispari == 3:
            return False
    else:
        count_dispari = 0  # Reset se trovi pari
    return self._verifica_da(nodo.successivo, trovato_pari_consecutivi, count_dispari)

'''
Scrivere un metodo che trova il minore
'''
def trova_minore(self):
    if self._testa is None:
        return None  # o lancia eccezione se la lista è vuota
    return self._trova_minore_da(self._testa, self._testa.info)
def _trova_minore_da(self, nodo, minore):
    if nodo is None:
        return minore
    if nodo.info < minore:
        minore = nodo.info
    return self._trova_minore_da(nodo.successivo, minore)

'''
Scrivere un metodo somma_dispari(self) che restituisce la somma di tutti gli elementi dispari nella lista.
'''
def somma_dispari(self):
    return self._somma_dispari_da(self._testa, 0)

def _somma_dispari_da(self, nodo, somma):
    if nodo is None:
        return somma
    if nodo.info % 2 == 1:
        somma += nodo.info
    return self._somma_dispari_da(nodo.successivo, somma)

'''
Scrivere un metodo tutti_pari(self) che restituisce True se tutti i valori della lista sono pari, False altrimenti.
'''
def tutti_pari(self):
    if self._testa is None:
        return False
    return self._verifica_da(self._testa)

def _verifica_da(self, nodo):
    if nodo is None:
        return True
    if nodo.info % 2 == 1:
        return False
    return self._verifica_da(nodo.successivo)

'''
Scrivere un metodo conta_valori(self, x) che conta quante volte compare x nella lista.
'''
def conta_valori(self, x):
    if self._nodo is None:
        return 0
    return self._conta_valori_da(self._testa, x, 0)

def _conta_valori_da(self, nodo, x, count):
    if nodo is None:
        return count
    if nodo.info == x:
        count += 1
    return self._conta_valori_da(nodo.successivo, x, count)

'''
Scrivere un metodo somma_finché_pari(self) che restituisce la somma dei primi elementi finché sono pari.
'''
def somma_finche_pari(self):
    if self._testa is None:
        return 0
    return self._somma_finche_pari_da(self._testa, 0)

def _somma_finche_pari_da(self, nodo, somma):
    if nodo is None or nodo.info % 2 == 1:
        return somma
    somma += nodo.info
    return self._somma_finche_pari_da(nodo.successivo, somma)

'''
Scrivere un metodo verifica(self) che restituisce True se i numeri pari sono più di quelli dispari nella lista.
'''
def verifica(self):
    if self._testa is None:
        return False
    pari, dispari = _verifica_da(self._testa, 0 ,0)
    return pari > dispari

def _verifica_da(self, nodo, countP, countD):
    if nodo is None:
        return False
    if nodo.info % 2 == 0:
        countP += 1
    else:
        countD += 1
    return self._verifica_da(nodo.successivo, countP, countD)

'''
Scrivere un metodo massimo(self) che restituisce il valore massimo presente nella lista.
'''
def massimo(self):
    if self._testa is None:
        return None
    return self._massimo_da(self._testa, self._testa.inf0)

def _massimo_da(self, nodo, max):
    if nodo is None:
        return max
    if nodo.successivo.info > nodo.info:
        max = nodo.successivo.info
    return self._massimo_da(nodo.successivo, max)

    