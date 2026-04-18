# Simulazione d'esame (gia fatta v3.0)
from listaconcatenata import ListaConcatenata, Iteratore
from alberobinario import AlberoBinarioRicerca, Nodo

class Attore:
    def __init__(self, nome, generi_preferiti : ListaConcatenata):
        self.nome = nome
        self.generi_preferiti = generi_preferiti
    def getNome(self):
        return self.nome
    def getGeneriPreferiti(self):
        return self.generi_preferiti
    def __eq__(self, other):
        return self.nome == other.nome
    def __repr__(self):
        return f'{self.nome} {self.generi_preferiti}'

class Film:
    def __init__(self, titolo, attori : ListaConcatenata, apparizioni : ListaConcatenata, genere, durata):
        self.titolo = titolo
        self.attori = attori
        self.apparizioni = apparizioni
        self.genere = genere
        self.durata = durata
    def getTitolo(self):
        return self.titolo
    def getAttori(self):
        return self.attori
    def getApparizioni(self):
        return self.apparizioni
    def getGenere(self):
        return self.genere
    def getDurata(self):
        return self.durata
    def __eq__(self, other):
        return self.titolo == other.titolo
    def __repr__(self):
        return f'{self.titolo} {self.attori} {self.apparizioni}'

class Sistema:
    def __init__(self, listaAttori: ListaConcatenata, listaFilm : ListaConcatenata):
        self.listaAttori = listaAttori
        self.listaFilm = listaFilm

    '''
    attore_max_durata(self, gen) che restituisce il nome dell'attore che ha la massima durata complessiva di scene
    girate in film di genere gen
    '''
    def attore_max_duarata(self, gen):
        res = None
        attori_durate = {}
        iter_film = Iteratore(self.listaFilm)
        while not iter_film.finito():
            film = next(iter_film)
            if film.getGenere() == gen:
                lista_attori = film.getAttori()
                durata_film = film.getDurata()
                iter_attori = Iteratore(lista_attori)
                while not iter_attori.finito():
                    attore = next(iter_attori)
                    attori_durate[attore] = attori_durate.get(attore, 0) + durata_film
        max_durata = -1
        for attore, durata in attori_durate.items():
            if durata > max_durata:
                max_durata = durata
                res = attore.getNome()
        return res

                
    '''
    cast_adeguato(self) che restituisce la lista dei titoli dei film il cui cast è adeguato, ossia film in cui tutti gli attori hanno 
    tra i generi preferiti il genere del film
    '''
    def cast_adeguato(self):
        res = ListaConcatenata()
        iter_film = Iteratore(self.listaFilm)
        while not iter_film.finito():
            film = next(iter_film)
            genere_film = film.getGenere()
            lista_attori = film.getAttori()
            cast_adeguato = True
            iter_attori = Iteratore(lista_attori)
            while not iter_attori.finito():
                attore = next(iter_attori)
                lista_generi_attore = attore.getGeneriPreferiti()
                trovato = False
                iter_generi = Iteratore(lista_generi_attore)
                while not iter_generi.finito():
                    genere = next(iter_generi)
                    if genere == genere_film:
                        trovato = True
                        break
                if not trovato:
                    cast_adeguato = False
            if cast_adeguato:
                res.aggiungi_in_coda(film.getTitolo())
        return res
                        
    
    '''
    attori_simili(self, nome_attore) che restituisce la lista dei nomi degli attori che hanno partecipato a tutti
    i film a cui ha partecipato l'attore il cui nome è passato come argomento
    '''
    def attori_simili(self, nome_attore):
        res = ListaConcatenata()
        attore_ref = None
        iter_attori = Iteratore(self.listaAttori)
        while not iter_attori.finito():
            attore = next(iter_attori)
            if attore.getNome() == nome_attore:
                attore_ref = attore
                break
        film_attore_ref = set()
        iter_film = Iteratore(self.listaFilm)
        while not iter_film.finito():
            film = next(iter_film)
            lista_attori = Iteratore(film.getAttori())
            while not iter_attori.finito():
                att = next(iter_attori)
                if att.getNome() == attore_ref.getNome():
                    film_attore_ref.add(film.getNome())
        iter_attori = Iteratore(self.listaAttori)
        while not iter_attori.finito():
            attore = next(iter_attori)
            if attore.getNome() == nome_attore:
                continue
            ha_partecipato = True
            for film_ref in film_attore_ref:
                trovato = False
                iter_attori_film = Iteratore(film_attore_ref.getAttori())
                while not iter_attori_film.finito():
                    a = next(iter_attori_film)
                    if a == attore:
                        trovato = True
                        break
                if not trovato:
                    ha_partecipato = False
            if ha_partecipato:
                res.aggiungi_in_coda(res.aggiungi_in_coda(attore.getNome()))
        return res
    
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
    if nodo.figlio_sinistro is None and nodo.figlio_destro is not None:
        if not self.contiene_dispari(nodo.figlio_desto):
            return False
    return self._verifica_da(nodo.figlio_sinistro) and self._verifica_da(nodo.figlio_destro)

def contiene_pari(self, nodo):
    if nodo is None:
        return False
    if nodo.info % 2 == 0:
        return True
    return self.contiene_pari(nodo.figlio_sinistro) or self._contiene_pari(nodo.figlio_destro)

def contiene_dispari(self, nodo):
    if nodo is None:
        return False
    if nodo.info % 2 != 0:
        return True
    return self.contiene_dispari(nodo.figlio_sinistro) or self._contiene_dispari(nodo.figlio_destro)




