'''
20/06

In base alle specifiche riportate di seguito, si implementi in Java un programma per la gestione di informazioni relative
alla produzione farmaceutica europea.
Le informazioni sono memorizzate all’interno della classe Gestione mediante tre strutture dati: un ArrayList farmaci
contenente istanze della classe Farmaco, un ArrayList produttori contenente istanze della classe Produttore ed un
ArrayList principiAttivi contenente l’elenco dei principi attivi usati nei farmaci, rappresentati semplicemente dal
proprio nome (e quindi codificati come stringhe).
Ogni produttore è identificato da un codice intero ed è caratterizzato da un nome ed una nazione.
Ogni farmaco è identificato da un codice intero ed è caratterizzato da un nome, dal codice del produttore, dal prezzo
(che assumiamo double) e dall’insieme dei principi attivi contenuti nel farmaco.
Si implementino in Java le classi Farmaco, Produttore e Gestione. Oltre a scrivere eventuali metodi che si ritengano
necessari per realizzare l’applicazione, occorre fornire almeno i seguenti metodi nella classe Gestione:
 public String farmacoCaro(String p). Il metodo restituisce, fra i farmaci realizzati con il principio attivo p, il nome
del farmaco con costo maggiore.
 public ArrayList<Produttore> esclusivisti(). Il metodo restituisce l’elenco dei produttori che producono almeno un
farmaco per cui non esiste un equivalente (due farmaci sono equivalenti quando contengono gli stessi principi
attivi) realizzato da un altro produttore.
 public ArrayList<String> universali(). Il metodo restituisce i principi attivi usati in almeno un farmaco di un
produttore di ogni nazione.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Farmaco:
    def __init__(self, codice, nome, produttore, prezzo, principi : ListaConcatenata):
        self.codice = codice
        self.nome = nome
        self.produttore = produttore
        self.prezzo = prezzo
        self.principi = principi
    def getCodice(self):
        return self.codice
    def getNome(self):
        return self.nome
    def getProduttore(self):
        return self.produttore
    def getPrezzo(self):
        return self.prezzo
    def getPrincipi(self):
        return self.principi
    def __eq__(self, other):
        return self.codice == other.codice
    def __repr__(self):
        return self.nome

class Produttore:
    def __init__(self, codice, nome, nazione):
        self.codice = codice
        self.nome = nome
        self.nazione = nazione

    def getCodice(self):
        return self.codice
    def getNome(self):
        return self.nome
    def getNazione(self):
        return self.nazione

    def __eq__(self, other):
        return self.codice == other.codice

    def __repr__(self):
        return self.nome

class Sistema:
    def __init__(self, farmaci : list[Farmaco], produttori: list[Produttore]):
        self.farmaci = farmaci
        self.produttori = produttori

    '''
    public String farmacoCaro(String p). Il metodo restituisce, fra i farmaci realizzati con il principio attivo p, il nome
    del farmaco con costo maggiore.
    '''
    def farmacoCaro(self, p):
        res = None
        max_prezzo = -1
        for farm in self.farmaci:
            farmaco = farm.getNome()
            principi = farm.getPrincipi()
            iter_principi = Iteratore(principi)
            while not iter_principi.finito():
                principio = next(iter_principi)
                if principio == p:
                    prezzo_farmaco = farm.getPrezzo()
                    if prezzo_farmaco > max_prezzo:
                        max_prezzo = prezzo_farmaco
                        res = farmaco
        return res
    
    '''
    public ArrayList<Produttore> esclusivisti(). Il metodo restituisce l’elenco dei produttori che producono almeno un
    farmaco per cui non esiste un equivalente (due farmaci sono equivalenti quando contengono gli stessi principi
    attivi) realizzato da un altro produttore.
    '''
    def esclusivisti(self):
        res = ListaConcatenata()
        dizionario_produttori_principi = {}
        for farmaco in self.farmaci:
            produttore = farmaco.getProduttore()
            principi_set = set()
            iter_principi = Iteratore(farmaco.getPrincipi)
            while not iter_principi.finito():
                principio = next(iter_principi)
                principi_set.add(principio)
            key = frozenset(principi_set) # serve per usarlo come chiave nel dizionario
            if key not in dizionario_produttori_principi:
                dizionario_produttori_principi[key] = set()
            dizionario_produttori_principi[key].add(produttore)
        produttori_esclusivi = set()
        for produttori in dizionario_produttori_principi.values():
            if len(produttori) == 1:
                produttori_esclusivi.update(produttori)
        for produttore in produttori_esclusivi:
            res.aggiungi_in_coda(produttore)
        return res
    
    '''
    public ArrayList<String> universali(). Il metodo restituisce i principi attivi usati in almeno un farmaco di un
    produttore di ogni nazione.
    '''
    def universali(self):
        res = ListaConcatenata()
        d = {}
        for farmaco in self.farmaci:
            principi = farmaco.getPrincipi()
            iteratore = Iteratore(principi)
            while not iteratore.finito():
                principio = next(iteratore)
                if principio not in d:
                    d[principio] = set()
                d[principio].add(farmaco)
        set_tutti_paesi = set()
        for produttore in self.produttori:
            set_tutti_paesi.add(produttore.getNazione())
        for coppia in d.items():
            principio_candidato = coppia[0]
            insieme_paesi = coppia[1]
            if len(insieme_paesi) == len(set_tutti_paesi):
                res.aggiungi_in_coda(principio_candidato)
        return res

