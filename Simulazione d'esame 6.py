'''
17/06

In base alle specifiche riportate di seguito, si implementi in Java un sistema di supporto alla gestione delle
informazioni relative a pubblicazioni scientifiche. In particolare, occorre tenere traccia della lista degli autori
(istanze della classe Autore) e della lista delle loro pubblicazioni (istanze della classe Pubblicazione).
Ciascun Autore è identificato da un nome ed è caratterizzato dalla città di residenza.
Ogni Pubblicazione è identificata da un codice ed è caratterizzata dal titolo, dalla lista dei nomi degli autori
e da una data (rappresentata come intero).
Si implementino in Java le classi Autore, Pubblicazione e Sistema. Oltre a scrivere eventuali metodi che si
ritengono necessari per implementare l’applicazione, occorre fornire almeno i seguenti metodi nella classe
Sistema:
1. public ArrayList<String> pubblicazioniCitta(String s). Il metodo restituisce la lista dei codici delle
pubblicazioni scritte solo da autori residenti nella città s.
2. public ArrayList<Autore> individuali(int d1, int d2). Il metodo restituisce la lista degli autori di
pubblicazioni individuali (cioè con un singolo autore) nel periodo compreso tra la data d1 e la data
d2.
3. public ArrayList<Pubblicazione> coautori(Autore a, Autore b). Il metodo restituisce la lista delle
pubblicazioni scritte congiuntamente dagli autori a e b (eventualmente insieme ad altri), ordinata
secondo la data di pubblicazione.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Pubblicazione:
    def __init__(self, codice, titolo, autori : ListaConcatenata, data):
        self.codice = codice
        self.titolo = titolo
        self.autori = autori
        self.data = data
    def getCodice(self):
        return self.codice
    def getTitolo(self):
        return self.titolo
    def getAutori(self):
        return self.autori
    def getData(self):
        return self.data
    def __eq__(self, other):
        return self.codice == other.codice
    def __repr__(self):
        return self.titolo
    def __hash__(self):
        return hash(self.codice)

class Autore:
    def __init__(self,nome, citta):
        self.nome = nome
        self.citta = citta
    def __eq__(self, other):
        return self.nome == other.nome
    def __repr__(self):
        return self.nome
    def getNome(self):
        return self.nome
    def getCitta(self):
        return self.citta
    def __hash__(self):
        return hash(self.nome)

class Sistema:
    def __init__(self, autori : list[Autore], pubblicazioni : list[Pubblicazione]):
        self.autori = autori
        self.pubblicazioni = pubblicazioni

    '''
    1. public ArrayList<String> pubblicazioniCitta(String s). Il metodo restituisce la lista dei codici delle
    pubblicazioni scritte solo da autori residenti nella città s.
    '''
    def pubblicazioniCitta(self, s):
        res = ListaConcatenata()
        for pubblicazioni in self.pubblicazioni:
            pubblicazione = pubblicazioni.getCodice()
            autori = pubblicazioni.getAutori()
            valido = True
            iter_autori = Iteratore(autori)
            while not iter_autori.finito():
                autore = next(iter_autori)
                residenza_autore = autore.getCitta()
                if residenza_autore != s:
                    valido = False
                    break
            if valido:
                res.aggiungi_in_coda(pubblicazione)
        return res
    
    '''
    2. public ArrayList<Autore> individuali(int d1, int d2). Il metodo restituisce la lista degli autori di
    pubblicazioni individuali (cioè con un singolo autore) nel periodo compreso tra la data d1 e la data
    d2.
    '''
    def individuali(self, d1, d2):
        res = ListaConcatenata()
        for pubblicazioni in self.pubblicazioni:
            pubblicazione = pubblicazioni.getCodice()
            data_pubblicazione = pubblicazioni.getData()
            if data_pubblicazione >= d1 and data_pubblicazione <= d2:
                lista_autori = pubblicazioni.getAutori()
                if len(lista_autori) == 1:
                    iter_autori = Iteratore(lista_autori)
                    while not iter_autori.finito():
                        autore = next(iter_autori)
                        res.aggiungi_in_coda(autore)
        return res
    
    '''
    3. public ArrayList<Pubblicazione> coautori(Autore a, Autore b). Il metodo restituisce la lista delle
    pubblicazioni scritte congiuntamente dagli autori a e b (eventualmente insieme ad altri), ordinata
    secondo la data di pubblicazione.
    '''
    def coautori(self, a: Autore, b: Autore):
        res = []
        for pubblicazioni in self.pubblicazioni:
            nomi_autori = pubblicazioni.getAutori()
            if a.getNome() in nomi_autori and b.getNome() in nomi_autori:
                res.append(pubblicazioni)
        res.sort(key = lambda p: p.getData())
        return res