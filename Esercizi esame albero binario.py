from alberobinario import AlberoBinarioRicerca, Nodo

'''
Si arricchisca la classe AlberoBinarioRicerca sviluppata durante il corso con un metodo verifica(self) che restituisce True se e solo se: 
per ogni nodo avente entrambi i figli e contenente un valore pari, il sottoalbero sinistro contiene almeno un altro valore pari; 
per ogni nodo avente entrambi i figli e contenente un valore dispari, il sottoalbero destro contiene almeno un altro valore dispari. 
Il metodo verifica dovrà essere ricorsivo o invocare un opportuno metodo ricorsivo.  
'''
def verifica(self):
    return self._verifica_da(self._radice)

def _verifica_da(self, nodo):
    if nodo is None:
        return True
    if nodo.figlio_sinistro is not None and nodo.figlio_destro is not None:
        if nodo.info % 2 == 0:
            if not self._contiene_pari(nodo.figlio_sinistro):
                return False
        else:
            if not self._contiene_dispari(nodo.figlio_destro):
                return False
    return self._verifica_da(nodo.figlio_sinistro) and self._verifica_da(nodo.figlio_destro)

def _contiene_pari(self, nodo):
    if nodo is None:
        return False
    if nodo.info % 2 == 0:
        return True
    return self._contiene_pari(nodo.figlio_sinistro) or self._contiene_pari(nodo.figlio_destro)

def _contiene_dispari(self, nodo):
    if nodo is None:
        return False
    if nodo.info % 2 != 0:
        return True
    return self._contiene_dispari(nodo.figlio_sinistro) or self._contiene_dispari(nodo.figlio_destro)

'''
Per ogni nodo che ha solo il figlio sinistro, il valore del figlio sinistro deve essere minore di quello del nodo.
Per ogni nodo che ha solo il figlio destro, il valore del figlio destro deve essere maggiore di quello del nodo.
'''
def verifica(self):
    return self._verifica_da(self._radice)

def _verifica_da(self, nodo):
    if nodo is None:
        return True
    if nodo.figlio_sinistro is not None and nodo.figlio_destro is None:
        if nodo.figlio_sinistro.info >= nodo.info:
            return False
    if nodo.figlio_destro is not None and nodo.figlio_sinistro is None:
        if nodo.figlio_destro.info <= nodo.info:
            return False
    return self._verifica_da(nodo.figlio_sinistro) and self._verifica_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_due_figli_pari(self) che restituisce True se per ogni nodo con entrambi i figli, il valore del nodo è pari, e almeno uno dei due figli ha valore pari.
Se almeno un nodo con entrambi i figli non rispetta questa regola, deve restituire False.
'''
def verifica_due_figli_pari(self):
    return self._verifica_due_figli_pari_da(self._radice)

def _verifica_due_figli_pari_da(self, nodo):
    if nodo is None: 
        return True
    if nodo.figlio_sinistro is not None and nodo.figlio_destro is not None:
        if nodo.info % 2 != 0:
            return False
        else:
            if nodo.figlio_sinistro.info % 2 != 0 and nodo.figlio_destro.info % 2 != 0:
                return False
    return self._verifica_due_figli_pari_da(nodo.figlio_sinistro) and self._verifica_due_figli_pari_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_albero_dispari(self) che restituisce True se tutti i valori presenti nell’albero sono dispari, False altrimenti.
'''
def verifica_albero_dispari(self):
    return self._verifica_albero_dispari_da(self._radice)

def _verifica_albero_dispari_da(self, nodo):
    if nodo is None:
        return True
    if nodo.info % 2 == 0:
        return False
    return self._verifica_albero_dispari_da(nodo.figlio_sinistro) and self._verifica_albero_dispari_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_nodi_senza_figli(self) che restituisce True se tutti i nodi foglia (cioè senza figli) 
contengono valori maggiori di 10.
'''
def verifica_nodi_senza_figli(self):
    return self._verifica_nodi_senza_figli_da(self._radice)

def _verifica_nodi_senza_figli_da(self, nodo):
    if nodo is None:
        return True
    if nodo.figlio_sinistro is None and nodo.figlio_destro is None:
        if nodo.info <= 10:
            return False
    return self._verifica_nodi_senza_figli_da(nodo.figlio_sinistro) and self._verifica_nodi_senza_figli_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_figli_sinistri_dispari(self) che restituisce True se tutti 
i nodi che hanno un figlio sinistro contengono un valore dispari, False altrimenti.
'''
def verifica_figli_sinistri_dispari(self):
    return self._verifica_figli_sinistri_dispari_da(self._radice)

def _verifica_figli_sinistri_dispari_da(self, nodo):
    if nodo is None: 
        return True
    if nodo.figlio_sinistro is not None:
        if nodo.info % 2 == 0:
            return False
    return self._verifica_figli_sinistri_dispari_da(nodo.figlio_sinistro) and self._verifica_figli_sinistri_dispari_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_foglie_pari(self) che restituisce True se tutti i nodi foglia contengono un valore pari, False altrimenti.
'''
def verifica_foglie_pari(self):
    return self._verifica_foglie_pari_da(self._radice)

def _verifica_foglie_pari_da(self, nodo):
    if nodo is None:
        return True
    if nodo.figlio_sinistro is None and nodo.figlio_destro is None:
        if nodo.info % 2 != 0:
            return False
    return self._verifica_foglie_pari_da(nodo.figlio_sinistro) and self._verifica_foglie_pari_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_figli_sinistro_maggiore(self) che restituisce True se per ogni nodo che ha un figlio sinistro, 
il valore del figlio sinistro è sempre maggiore del valore del nodo, False altrimenti.
'''
def verifica_figli_sinistro_maggiore(self):
    return self._verifica_figli_sinistro_maggiore_da(self._radice)

def _verifica_figli_sinistro_maggiore_da(self, nodo):
    if nodo is None:
        return True
    if nodo.figlio_sinistro is not None:
        if nodo.figlio_sinistro.info <= nodo.info:
            return False
    return self._verifica_figli_sinistro_maggiore_da(nodo.figlio_sinistro) and self._verifica_figli_sinistro_maggiore_da(nodo.figlio_destro)

'''
Scrivi un metodo verifica_sottoalbero_sinistro_contiene_valore(self, val) che restituisce 
True se in ogni sottoalbero sinistro di ogni nodo è presente almeno un nodo con valore val, False altrimenti.
'''
def verifica_sottoalbero_sinistro_contiene_valore(self, val):
    return self._verifica_sottoalbero_sinistro_contiene_valore_da(self._radice, val)

def _verifica_sottoalbero_sinistro_contiene_valore_da(self, nodo, val):
    if nodo is None:
        return False
    if nodo.figlio_sinistro is not None:
            if not contiene(nodo.figlio_sinistro, val):
                return False
    return self._verifica_sottoalbero_sinistro_contiene_valore_da(nodo.figlio_sinistro, val) and self._verifica_sottoalbero_sinistro_contiene_valore_da(nodo.figlio_destro, val)

def contiene(self, nodo, val):
    if nodo is None:
        return False
    if nodo.info == val:
        return True
    return self.contiene(nodo.figlio_sinistro, val) or self.contiene(nodo.figlio_destro, val)

'''
Scrivi un metodo verifica_figli_destri_pari(self) che restituisce True se tutti i nodi che hanno un 
figlio destro contengono un valore pari, False altrimenti.
'''
def verifica_figli_destri_pari(self):
    return self._verifica_figli_destri_pari_da(self._radice)

def _verifica_figli_destri_pari_da(self, nodo):
    if nodo is None:
        return True
    # Se il nodo ha figlio destro, allora il nodo deve essere pari
    if nodo.figlio_destro is not None and nodo.info % 2 != 0:
        return False
    return self._verifica_figli_destri_pari_da(nodo.figlio_sinistro) and self._verifica_figli_destri_pari_da(nodo.figlio_destro)

'''
Si arricchisca la classe AlberoBinarioRicerca sviluppata durante il corso con un metodo verifica(self) che restituisce True
se e solo se:
• per ogni nodo avente solo il figlio sinistro, il sottoalbero sinistro contiene almeno un valore pari;
• per ogni nodo avente solo il figlio destro, il sottoalbero destro contiene almeno un valore dispari.
Il metodo verifica dovrà essere ricorsivo o invocare un opportuno metodo ricorsivo.
'''
def verifica(self):
    return self._verifica_da(self._radice)

def _verifica_da(self, nodo):
    if nodo is None:
        return True
    if nodo.figlio_sinistro is not None and nodo.figlio_destro is None:
        if not self.contiene_pari(nodo.figlio_sinistro):
            return False
    if nodo.figlio_sinistro is None and nodo.figlio_destor is not None:
        if not self.contiene_dispari(nodo.figlio_destro):
            return False
    return self._verifica_da(nodo.figlio_sinistro) and self.verifica_da(nodo.figlio_destro)

def contiene_pari(self, nodo):
    if nodo is None:
        return False
    if nodo.info % 2 == 0:
        return True
    return self.contiene_pari(nodo.figlio_sinistro) or self.contiene_pari(nodo.figlio_destro)

def contiene_dispari(self, nodo):
    if nodo is None: 
        return False
    if nodo.info % 2 != 0:
        return False
    return self.contiene_dispari(nodo.figlio_sinistro) or self.contiene_dispari(nodo.figlio_destro)
        


