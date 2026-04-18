'''
Traccia 3

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti unità di personale
sanitario (medici e infermieri) e interventi chirurgici. Si supponga che siano definite le classi Personale e Intervento,
che forniscono i seguenti metodi:
Classe Personale:
• get_nome(self), che restituisce il nome che identifica l’unità di personale.
• get_tipo(self), che restituisce True se l’unità di personale è un medico, False se è un infermiere.
• get_unita_sotto_controllo(self), che restituisce la lista dei nomi delle unità di personale sotto il controllo
dell’unità di personale rappresentata dall’oggetto self.
• __eq__(self, other)
• __repr__(self)
Classe Intervento:
• get_codice(self), che restituisce il codice che identifica l’intervento chirurgico.
• get_equipe(self), che restituisce la lista dei nomi delle unità di personale che hanno preso parte all’intervento.
• get_ruoli(self), che restituisce la lista dei ruoli avuti nell’intervento delle unità di personale restituiti dal
metodo get_equipe(self). Si assuma che il ruolo in posizione i della lista restituita da get_ruoli(self) si riferisce
all’unità di personale nella posizione i della lista restituita da get_equipe(self).
• get_durata(self), che restituisce la durata (in ore) dell’intervento.
• __eq__(self, other)
• __repr__(self)
La classe Sistema contiene le liste lista_personale delle unità di personale e lista_interventi degli interventi chirurgici.
Oltre ad eventuali metodi che si ritengano necessari, si includano almeno i seguenti metodi nella classe:
• verifica(self). Il metodo restituisce True se e solo se non esistono unità di personale che hanno sotto il proprio
controllo unità di personale di tipo diverso dal proprio (medico o infermiere). Si noti che un’unità di personale
che non controlla alcuna altra unità soddisfa tale condizione.
• medico_frequente_con_ruolo(self, ruolo). Il metodo restituisce il nome dell’unità di personale di tipo medico
che ha partecipato al maggior numero di interventi nel ruolo passato come argomento. Se più medici
soddisfano la condizione, il metodo restituisce uno qualsiasi di essi.
• durata_media(self, lp). Il metodo restituisce la durata media degli interventi a cui ha partecipato almeno una
delle unità di personale di tipo medico tra quelle riportate nella lista lp. Se nessun intervento soddisfa il criterio,
il metodo restituisce -1. Si noti che la lista lp contiene oggetti della classe Personale, non stringhe.
'''
from listaconcatenata import ListaConcatenata

class Personale:
    def __init__(self, nome, tipo, listaUnita):
        self.nome=nome
        self.tipo=tipo
        self.listaUnita=listaUnita

    def __repr__(self):
        if (self.tipo):
            return f'Personale: {self.nome} - Tipo: Medico, Lista Unità: {self.listaUnita}'
        else:
            return f'Personale: {self.nome} - Tipo: Infermiere, Lista Unità: {self.listaUnita}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Personale):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi richiesti:

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo

    def get_unita_sotto_controllo(self):
        return self.listaUnita

class Intervento:
    def __init__(self, codice, listaEquipe, listaRuoli, durata):
        self.codice=codice
        self.listaEquipe=listaEquipe
        self.listaRuoli=listaRuoli
        self.durata=durata

    def __repr__(self):
        return f'Intervento: {self.codice} - Equipe: {self.listaEquipe}, Lista Ruoli: {self.listaRuoli}, Durata: {self.durata}h'

    def __eq__(self, other):
        if other is None or not isinstance(other, Intervento):
            return False
        if other is self:
            return True
        return self.codice==other.codice

    #Metodi richiesti:

    def get_codice(self):
        return self.listaEquipe

    def get_equipe(self):
        return self.listaEquipe

    def get_ruoli(self):
        return self.listaRuoli

    def get_durata(self):
        return self.durata

class Sistema:
    def __init__(self, listaPersonale, listaInterventi):
        self.listaPersonale=listaPersonale
        self.listaInterventi=listaInterventi

    '''
    • verifica(self). Il metodo restituisce True se e solo se non esistono unità di personale che hanno sotto il proprio
    controllo unità di personale di tipo diverso dal proprio (medico o infermiere). Si noti che un’unità di personale
    che non controlla alcuna altra unità soddisfa tale condizione.
    '''
    def verifica(self):
        for personale in self.listaPersonale:
            tipo = personale.get_tipo()
            lista_unita = personale.get_unita_sotto_controllo()
            for pers in lista_unita:
                if pers.get_tipo() != tipo:
                    return False
        return True
    
    '''
    • medico_frequente_con_ruolo(self, ruolo). Il metodo restituisce il nome dell’unità di personale di tipo medico
    che ha partecipato al maggior numero di interventi nel ruolo passato come argomento. Se più medici
    soddisfano la condizione, il metodo restituisce uno qualsiasi di essi.
    '''
    def medico_frequente_con_ruolo(self, ruolo):
        res = None
        d = {}
        for intervento in self.listaInterventi:
            lista_equipe = intervento.get_equipe()
            lista_ruoli = intervento.get_ruoli()
            for medico, r in zip(lista_equipe, lista_ruoli):
                if ruolo == r:
                    d[medico] = d.get(medico, 0) + 1
        return max(d, key=d.get)
    
    '''
    • durata_media(self, lp). Il metodo restituisce la durata media degli interventi a cui ha partecipato almeno una
    delle unità di personale di tipo medico tra quelle riportate nella lista lp. Se nessun intervento soddisfa il criterio,
    il metodo restituisce -1. Si noti che la lista lp contiene oggetti della classe Personale, non stringhe. 
    '''
    def durata_media(self, lp):
        durata_totale = 0
        count = 0
        set_lp = set(lp)  # per accesso rapido
        for intervento in self.listaInterventi:
            # ottengo l'equipe (lista di Personale) di ogni intervento
            equipe = intervento.get_equipe()
            # verifico se almeno un medico in lp è nell'equipe di questo intervento
            # ricordando che lp è lista di Personale e vogliamo solo medici (get_tipo()==True)
            if any(personale in set_lp and personale.get_tipo() for personale in equipe):
                durata_totale += intervento.get_durata()
                count += 1
            if count == 0:
                return -1
        return durata_totale / count

