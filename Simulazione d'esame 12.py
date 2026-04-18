'''
Traccia 2

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti dipendenti e riunioni.
Si supponga che siano definite le classi Dipendente e Riunione, che forniscono i seguenti metodi:
Classe Dipendente:
• get_nome(self), che restituisce il nome che identifica il dipendente.
• get_argomenti_interesse(self), che restituisce la lista degli argomenti di cui il dipendente è esperto.
•
__eq__(self, other).
• __repr__(self).
Classe Riunione:
• get_codice(self), che restituisce il codice che identifica la riunione.
• get_partecipanti(self), che restituisce la lista dei nomi dei dipendenti che hanno partecipato alla riunione.
• get_argomenti_trattati(self), che restituisce la lista degli argomenti trattati durante la riunione.
• get_data(self), che restituisce la data (espressa mediante un intero) in cui si è tenuta la riunione.
• get_durata(self), che restituisce la durata (in ore) della riunione.
•
__eq__(self, other).
• __repr__(self).
La classe Sistema contiene le liste lista_dipendenti dei dipendenti e lista_riunioni delle riunioni. Oltre ad eventuali
metodi che si ritengano necessari, si includano almeno i seguenti metodi nella classe:
• argomento_frequente(self, d). Il metodo restituisce l'argomento che è stato trattato il maggior numero di volte
in riunioni tenute in date precedenti a d. Se più argomenti soddisfano la condizione, il metodo restituisce uno
qualsiasi di essi.
• dipendenti_piu_attivi(self, nome_dip), che restituisce la lista dei nomi distinti dei dipendenti che risultano
essere più attivi del dipendente con nome nome_dip. Un dipendente X è più attivo di un dipendente Y quando
sono soddisfatte entrambe le seguenti condizioni:
• la somma delle durate delle riunioni a cui ha partecipato X è maggiore della somma delle durate delle
riunioni a cui ha partecipato Y;
• X è esperto di tutti gli argomenti di cui Y è esperto.
• argomenti_no(self, nome_dip, d). Il metodo restituisce la lista degli argomenti di cui è esperto il dipendente di
nome nome_dip che non sono stati trattati in alcuna delle riunioni tenute in data d.
'''
from listaconcatenata import ListaConcatenata

class Dipendente:
    def __init__(self, nome, listaArgomenti):
        self.nome=nome
        self.listaArgomenti=listaArgomenti

    def __repr__(self):
        return f'Dipendente: {self.nome} - Argomenti: {self.listaArgomenti}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Dipendente):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi richiesti:

    def get_nome(self):
        return self.nome

    def get_argomenti_interesse(self):
        return self.listaArgomenti

class Riunione:
    def __init__(self, codice, listaPartecipanti, listaArgomenti, data, durata):
        self.codice=codice
        self.listaPartecipanti=listaPartecipanti
        self.listaArgomenti=listaArgomenti
        self.data=data
        self.durata=durata

    def __repr__(self):
        return f'Riunione: {self.codice} - Partecipanti:{self.listaPartecipanti} Argomenti: {self.listaArgomenti} In data: {self.data} Della durata di: {self.durata}h'

    def __eq__(self, other):
        if other is None or not isinstance(other, Riunione):
            return False
        if other is self:
            return True
        return self.codice==other.codice

    #Metodi richiesti:

    def get_codice(self):
        return self.codice

    def get_partecipanti(self):
        return self.listaPartecipanti

    def get_argomenti_trattati(self):
        return self.listaArgomenti

    def get_data(self):
        return self.data

    def get_durata(self):
        return self.durata

class Sistema:
    def __init__(self, listaDipendenti, listaRiunioni):
        self.listaDipendenti=listaDipendenti
        self.listaRiunioni=listaRiunioni

    '''
    • argomento_frequente(self, d). Il metodo restituisce l'argomento che è stato trattato il maggior numero di volte
    in riunioni tenute in date precedenti a d. Se più argomenti soddisfano la condizione, il metodo restituisce uno
    qualsiasi di essi.
    '''
    def argomento_frequente(self, d):
        res = None
        dict_argomento_num = {}
        for riunione in self.listaRiunioni:
            if riunione.get_data() < d:
                for argomento in riunione.get_argomenti_trattati():
                    dict_argomento_num[argomento] = dict_argomento_num(argomento, 0) + 1
        max_count = -1
        for argomento, count in dict_argomento_num.items():
            if count > max_count:
                max_count = count
                res = argomento
        return res
    
    '''
    • dipendenti_piu_attivi(self, nome_dip), che restituisce la lista dei nomi distinti dei dipendenti che risultano
    essere più attivi del dipendente con nome nome_dip. Un dipendente X è più attivo di un dipendente Y quando
    sono soddisfatte entrambe le seguenti condizioni:
    • la somma delle durate delle riunioni a cui ha partecipato X è maggiore della somma delle durate delle
    riunioni a cui ha partecipato Y;
    • X è esperto di tutti gli argomenti di cui Y è esperto.
    '''
    def dipendenti_piu_attivi(self, nome_dipendente):
        res = ListaConcatenata()
        dip_res = None
        for d in self.listaDipendenti:
            if d.get_nome() == nome_dipendente:
                dip_res = d
        argomenti_res = set(dip_res.get_argomenti_interesse())
        durata_ref = 0
        for riunione in self.listaRiunioni:
            if dip_res in riunione.get_partecipanti():
                durata_ref += riunione.get_durata()
        for d in self.listaDipendenti:
            if d == dip_res:
                continue
            durata_altro = 0
            for riunione in self.listaRiunioni:
                if d in riunione.get_partecipanti():
                    durata_altro += riunione.getDurata()
            argomenti_altro = set(d.get_argomenti_interesse())
            if durata_altro > durata_ref and argomenti_res.issubset(argomenti_altro): # confronta se ci sono tutti
                res.aggiungi_in_coda(d.get_nome())
        return res
    
    '''
    • argomenti_no(self, nome_dip, d). Il metodo restituisce la lista degli argomenti di cui è esperto il dipendente di
    nome nome_dip che non sono stati trattati in alcuna delle riunioni tenute in data d.
    '''
    def argomenti_no(self, nome_dip, d):
        res = ListaConcatenata()
        dip_res = None
        for dip in self.listaDipendenti:
            if dip.get_nome() == nome_dip:
                dip_res = dip
        argomenti_interesse_dip_res = set(dip_res.get_argomenti_interesse())
        argomenti_altro = set()
        for riunione in self.listaRiunioni:
            if riunione.get_data() == d:
                argomenti_altro.update(riunione.get_argomenti_trattati()) # aggiunge tutta la lista
        argomenti_trattati = argomenti_interesse_dip_res - argomenti_altro
        for arg in argomenti_trattati:
            res.aggiungi_in_coda(arg)
        return res
                    

