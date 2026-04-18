'''
13/06

In base alle specifiche riportate di seguito, si implementi in Java un sistema di supporto all’analisi dei dati
degli utenti del social network Twitter.
Il sistema (implementato in una classe Sistema) gestisce informazioni sui tweet (istanze della classe Tweet)
e sugli utenti (istanze della classe Utente). Ogni utente è identificato dal codice fiscale ed è caratterizzato
dalla città di residenza. Ogni tweet è identificato da un codice ed è caratterizzato dal codice fiscale dell’utente
che lo ha emesso, dalla data di emissione (rappresentata come intero), dalla città dalla quale è stato emesso
e da una lista di tag.
Si implementino le classi Sistema, Tweet e Utente. Oltre a scrivere eventuali metodi che si ritengono
necessari per implementare l’applicazione, occorre fornire almeno i seguenti metodi nella classe Sistema:
1. public ArrayList<String> cittaDiversa(). Il metodo restituisce la lista dei codici fiscali degli utenti che
hanno emesso tutti i tweet da una città diversa da quella di residenza.
2. public ArrayList<String> listaUtenti(). Il metodo restituisce la lista dei codici fiscali degli utenti che
hanno emesso almeno 2 tweet con tag diversi (cioè 2 tweet che non hanno tag in comune).
3. public String tagOfTheDay(int data). Il metodo restituisce il tag che, nella data passata in input, è
stato più utilizzato dagli utenti.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Utente:
    def __init__(self, id, residenza):
        self.id = id
        self.residenza = residenza
    def getId(self):
        return self.id
    def getResidenza(self):
        return self.residenza
    def __eq__(self, other):
        return self.id == other.id
    def __repr__(self):
        return self.id

class Tweet:
    def __init__(self, codice, idUtente, data, cittaEmissione, tag : ListaConcatenata):
        self.codice = codice
        self.idUtente = idUtente
        self.data = data
        self.cittaEmissione = cittaEmissione
        self.tag = tag
    def getCodice(self):
        return self.codice
    def getIdUtente(self):
        return self.idUtente
    def getData(self):
        return self.data
    def getCittaEmissione(self):
        return self.cittaEmissione
    def getTag(self):
        return self.tag
    def __eq__(self, other):
        return self.codice == other.codice
    def __repr__(self):
        return self.codice

class Sistema:
    def __init__(self, listaUtenti : list[Utente], listaTweet : list[Tweet]):
        self.listaUtenti = listaUtenti
        self.listaTweet = listaTweet

    '''
    public ArrayList<String> cittaDiversa(). Il metodo restituisce la lista dei codici fiscali degli utenti che
    hanno emesso tutti i tweet da una città diversa da quella di residenza.
    '''
    def cittaDiversa(self):
        res = ListaConcatenata()
        for utente in self.listaUtenti:
            id_utente = utente.getId()
            citta_residenza = utente.getResidenza()
            valido = True
            for tweet in self.listaTweet:
                if id_utente == tweet.getIdUtente():
                    if citta_residenza == tweet.getCittaEmissione():
                        valido = False
                        break
            if valido:
                res.aggiungi_in_coda(id_utente)
        return res
    
    '''
    2. public ArrayList<String> listaUtenti(). Il metodo restituisce la lista dei codici fiscali degli utenti che
    hanno emesso almeno 2 tweet con tag diversi (cioè 2 tweet che non hanno tag in comune).
    '''
    def listaUtenti(self):
        res = ListaConcatenata()
        for utente in self.listaUtenti:
            id_utente = utente.getId()
            lista_tag_utente = []
            for tweet in self.listaTweet:
                if id_utente == tweet.getIdUtente():
                    lista_tag_utente.append(tweet.getTag())
            if len(lista_tag_utente) >= 2 and self._verifica(lista_tag_utente):
                res.aggiungi_in_coda(id_utente)
        return res
    
    def _verifica(self, lista_tag_utente):
        set_tag = set()
        count_Len = 0
        for lista_tag in lista_tag_utente:
            iter_tag = Iteratore(lista_tag)
            while not iter_tag.finito():
                tag = next(iter_tag)
                set_tag.add(tag)
        for lista_tag in lista_tag_utente:
            count_Len += len(lista_tag)
        return len(set_tag) == count_Len
    
    '''
    3. public String tagOfTheDay(int data). Il metodo restituisce il tag che, nella data passata in input, è
    stato più utilizzato dagli utenti.
    '''
    def tagOfTheDay(self, data):
        d_count_for_tag = {}
        res = None
        max_count = 0
        for tweet in self.listaTweet:
            data_emissione = tweet.getData()
            if data_emissione == data:
                lista_tag = tweet.getTag()
                iter_tag = Iteratore(lista_tag)
                while not iter_tag.finito():
                    tag = next(iter_tag)
                    d_count_for_tag[tag] = d_count_for_tag.get(tag, 0) + 1
        for tag, count in d_count_for_tag.items():
            if count > max_count:
                max_count = count
                res = tag
        return res
                        
                    