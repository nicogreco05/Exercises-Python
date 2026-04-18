from listaconcatenata import ListaConcatenata, Iteratore
'''
Esercizio 1
Scrivi una funzione conta_lettere(stringa) che prende in input una stringa e 
restituisce un dizionario con quante volte appare ogni lettera (ignorando spazi e maiuscole/minuscole).
'''
def conta_lettere(stringa):
    d = {}
    for lettera in stringa:
        if lettera not in d:
            d[lettera] = 0
        d[lettera] += 1
    return d

'''
Esercizio 2
Hai una lista di tuple [(nome_studente, materia), ...] e devi creare un dizionario che associa a 
ogni materia la lista degli studenti che la studiano.
'''
def diz(self, listastudenti):
    d = {}
    for studente, materia in listastudenti:
        if materia not in d:
            d[materia] = []
        d[materia].append(studente)
    return d

'''
Eserczio 3
Scrivi una funzione conta_parole(frase) che prende una stringa e restituisce un dizionario con quante volte appare ogni parola.
'''
def conta_parole(frase):
    d = {}
    for parola in frase:
        if parola not in d:
            d[parola] = 0
        d[parola] += 1
    return d

'''
Eserczio 4
def registi3generi(self) che restituisce una lista dei nomi dei registi che hanno diretto film di almeno 3 generi diversi.
'''
class Regista:
    def __init__(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome

class Film:
    def __init__(self, titolo, regista, genere):
        self.titolo = titolo
        self.regista = regista  # oggetto Regista
        self.genere = genere
    def getTitolo(self):
        return self.titolo
    def getRegista(self):
        return self.regista
    def getGenere(self):
        return self.genere
# fatta da me
def registi3generi(self):
    res = ListaConcatenata()
    d = self._dizionario()
    for coppia in d.items():
        nome_regista = coppia[0]
        set_film = coppia[1]
        if len(set_film) == 3:
            res.aggiungi_in_coda(nome_regista)
    return res

def _dizionario(self):
    d = {}
    for film in self.listaFilm:
        regista = film.getRegista()
        genere = film.getGenere()
        if regista not in d:
            d[regista] = set()
        d[regista].add(genere)
    return d

# versione corretta
def _dizionario(self):
    d = {}
    for film in self.listaFilm:
        nome_regista = film.getRegista().getNome()
        genere = film.getGenere()
        if nome_regista not in d:
            d[nome_regista] = set()
        d[nome_regista].add(genere)  # questa va fuori dal if
    return d

def registi3generi(self):
    res = ListaConcatenata()
    d = self._dizionario()
    for nome_regista, generi in d.items():
        if len(generi) >= 3:  # usa >= 3 (almeno 3)
            res.aggiungi_in_coda(nome_regista)
    return res
    
