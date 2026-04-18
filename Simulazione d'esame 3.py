from listaconcatenata import ListaConcatenata, Iteratore

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
    def attore_max_durata(self, gen):
        res = None
        attori_durate = {}
        iter_film = Iteratore(self.listaFilm)
        while not iter_film.finito():
            film = next(iter_film)
            genere_film = film.getGenere()
            if genere_film == gen:
                attori = film.getAttori()
                durata = film.getDurata()
                iter_attori = Iteratore(attori)
                while not iter_attori.finito():
                    attore = next(iter_attori)
                    attori_durate[attore] = attori_durate.get(attore, 0) + durata
        max_durata = 0
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
            attori = film.getAttori()
            cast_adeguato = True
            iter_attori = Iteratore(attori)
            while not iter_attori.finito():
                attore = next(iter_attori)
                generi_preferiti = attore.getGeneriPreferiti()
                iter_generi_pref = Iteratore(generi_preferiti)
                trovato = False
                while not iter_generi_pref.finito():
                    genere_preferito = next(iter_generi_pref)
                    if genere_preferito == genere_film:
                        trovato = True
                        break
                if not trovato:
                    cast_adeguato = False
            if cast_adeguato:
                res.aggiungi_in_coda(attore)
        return res

    
    '''
    attori_simili(self, nome_attore) che restituisce la lista dei nomi degli attori che hanno partecipato a tutti
    i film a cui ha partecipato l'attore il cui nome è passato come argomento
    '''
    def attori_simili(self, nome_attore):
        res = ListaConcatenata()
        iter_film = Iteratore(self.listaFilm)
        while not iter_film.finito():
            film = next(iter_film)
            attori = film.getAttori()
            iter_attori = Iteratore(attori)
            ha_partecipato = True
            while not iter_attori.finito():
                attore = next(iter_attori)
                if nome_attore in film:
                    if not attore in film:
                        ha_partecipato = False
            if ha_partecipato:
                res.aggiungi_in_coda(attore)
        return res





