'''
Traccia 1

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti viaggi in autobus e
conducenti. Si supponga che siano definite le classi Viaggio e Conducente, che forniscono i seguenti metodi:
Classe Viaggio:
• get
_
codice(self), che restituisce il codice che identifica il viaggio.
• get
_
destinazione(self), che restituisce la destinazione del viaggio.
• get_durata(self), che restituisce la durata (in ore) del viaggio.
• get_num_passeggeri(self), che restituisce il numero di passeggeri che partecipano al viaggio.
• __eq__(self, other).
• __repr__(self).
Classe Conducente:
• get_nome(self), che restituisce il nome che identifica il conducente.
• get
_viaggi (self), che restituisce la lista dei codici dei viaggi gestiti dal conducente.
• __eq__(self, other).
• __repr__(self).
La classe Sistema contiene le liste lista_viaggi dei viaggi e lista_conducenti dei conducenti. Oltre ad eventuali metodi
che si ritengano necessari, si includano almeno i seguenti metodi nella classe:
• verifica(self, ore_min, passeggeri_max), che restituisce True se e solo se sono soddisfatte entrambe le seguenti
condizioni:
• nessun conducente ha un numero complessivo di ore inferiore a ore_min (il numero complessivo di
ore di un conducente è la somma delle durate dei viaggi gestiti dal conducente stesso);
• nessun viaggio ha un numero di passeggeri maggiore di passeggeri_max.
• destinazioni_richieste(self, passeggeri_min). Il metodo restituisce la lista delle destinazioni richieste – una
destinazione d è richiesta se soddisfa le seguenti condizioni:
• almeno 2 viaggi hanno destinazione d;
• il numero totale di passeggeri che partecipano a viaggi aventi destinazione d è maggiore di
passeggeri_min.
• conducenti_diversi(self, conducente). Il metodo restituisce la lista dei nomi distinti dei conducenti i cui viaggi
non hanno destinazioni in comune con i viaggi gestiti dal conducente con nome conducente.
'''
from listaconcatenata import ListaConcatenata

class Viaggio:
    def __init__(self, codice, destinazione, durata, numPasseggeri):
        self.codice=codice
        self.destinazione=destinazione
        self.durata=durata
        self.numPasseggeri=numPasseggeri

    def __repr__(self):
        return f'Viaggio: {self.codice} - Destinazione: {self.destinazione}, Durata: {self.durata}, Numero passeggeri: {self.numPasseggeri}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Viaggio):
            return False
        if other is self:
            return True
        return self.codice==other.codice

    #Metodi accessori
    def get_codice(self):
        return self.codice

    def get_destinazione(self):
        return self.destinazione

    def get_durata(self):
        return self.durata

    def get_num_passeggeri(self):
        return self.numPasseggeri

class Conducente:
    def __init__(self, nome, listaViaggi):
        self.nome=nome
        self.listaViaggi=listaViaggi

    def __repr__(self):
        return f'Conducente: {self.nome} - Lista viaggi: {self.listaViaggi}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Conducente):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi accessori
    def get_nome(self):
        return self.nome

    def get_viaggi(self):
        return self.listaViaggi

class Sistema:
    def __init__(self, listaViaggi, listaConducenti):
        self.listaViaggi=listaViaggi
        self.listaConducenti=listaConducenti

    '''
    • verifica(self, ore_min, passeggeri_max), che restituisce True se e solo se sono soddisfatte entrambe le seguenti
    condizioni:
    • nessun conducente ha un numero complessivo di ore inferiore a ore_min (il numero complessivo di
    ore di un conducente è la somma delle durate dei viaggi gestiti dal conducente stesso);
    • nessun viaggio ha un numero di passeggeri maggiore di passeggeri_max.
    '''
    def verifica(self, ore_min, passeggeri_max):
        for conducente in self.listaConducenti:
            ore_totali = 0
            for viaggio in conducente.get_viaggi():
                ore_totali += viaggio.get_durata()
                if ore_totali < ore_min:
                    return False
            for viaggio in self.listaViaggi:
                if viaggio.get_num_passeggeri() > passeggeri_max:
                    return False
        return True
    
    '''
    • destinazioni_richieste(self, passeggeri_min). Il metodo restituisce la lista delle destinazioni richieste – una
    destinazione d è richiesta se soddisfa le seguenti condizioni:
    • almeno 2 viaggi hanno destinazione d;
    • il numero totale di passeggeri che partecipano a viaggi aventi destinazione d è maggiore di
    passeggeri_min.
    '''
    def destinazioni_richieste(self, passeggeri_min):
        res = ListaConcatenata()
        dict_destinazioni_num = {}
        dic_destinazioni_num_passeggeri = {}
        for viaggio in self.listaViaggi:
            destinazione = viaggio.get_destinazione()
            num_passegeri = viaggio.get_num_passeggeri()
            dict_destinazioni_num[destinazione] = dict_destinazioni_num.get(destinazione, 0) + 1
            dic_destinazioni_num_passeggeri[destinazione] = dic_destinazioni_num_passeggeri.get(destinazione, 0) + num_passegeri
        for destinazione in dict_destinazioni_num:
            if dict_destinazioni_num[destinazione] >= 2 and dic_destinazioni_num_passeggeri[destinazione] > num_passegeri:
                res.aggiungi_in_coda(destinazione)
        return res
    
    '''
    • conducenti_diversi(self, conducente). Il metodo restituisce la lista dei nomi distinti dei conducenti i cui viaggi
    non hanno destinazioni in comune con i viaggi gestiti dal conducente con nome conducente.
    '''
    def conducenti_diversi(self, conducente):
        res = ListaConcatenata()
        destinazioni_conducente = set()
        for c in self.listaConducenti:
            if c.get_nome() == conducente:
                for viaggio in c.get_viaggi():
                    destinazioni_conducente.add(viaggio.get_destinazione())
                break
        for c in self.listaConducenti:
            if c.get_nome() != conducente:
                destinazioni_altro = set()
                for viaggio in c.get_viaggi():
                    destinazioni_altro.add(viaggio.get_destinazione())
                if destinazioni_conducente.isdisjoint(destinazioni_altro): # confronta se non ci sono dest comuni
                    res.aggiungi_in_coda(c.get_nome())
        return res
                


        

            

        


