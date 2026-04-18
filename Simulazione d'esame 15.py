'''
Simulazione d'esame 

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti un insieme di scienziati
e di progetti di ricerca in cui tali scienziati sono coinvolti. Si supponga che siano definite le classi Scienziato e
ProgettoDiRicerca, che forniscono i seguenti metodi:
Classe Scienziato:
• get_nome(self), che restituisce il nome che identifica lo scienziato.
• get_ambiti_ricerca(self), che restituisce la lista degli ambiti di ricerca in cui lo scienziato è attivo (ad es., “Fisica
Sperimentale”, “Informatica teorica”, ecc.)
•
__eq__(self, other).
• __repr__(self).
Classe ProgettoDiRIcerca:
• get
_
titolo(self), che restituisce il titolo che identifica il progetto di ricerca.
• get
_
team(self), che restituisce il team di ricerca del progetto, ossia la lista dei nomi degli scienziati che hanno
contribuito al progetto di ricerca.
• get
_
contributi(self), che restituisce la lista dei contributi (in termini di tempo dedicato) dei membri del team
al progetto. L’elemento in posizione i della lista dei contributi indica il tempo dedicato alle attività del progetto
di ricerca dallo scienziato in posizione i nella lista restituita da get_team.
• get
_ambito_principale(self), che restituisce il principale ambito di ricerca del progetto (ad es., “Fisica
Sperimentale”, “Informatica teorica”, ecc.)
•
__eq__(self, other).
• __repr__(self).
La classe Sistema contiene le liste listaScienziati degli scienziati e listaProgetti dei progetti di ricerca. Oltre ad eventuali
metodi che si ritengano necessari, si includano almeno i seguenti metodi nella classe:
• scienziato
_max_contributo(self, amb). Il metodo restituisce il nome dello scienziato che ha fornito il massimo
contributo complessivo in progetti di ricerca nell’ambito amb. Se più scienziati soddisfano la condizione, il
metodo restituisce uno qualsiasi di essi
• team
_
coerente(self), che restituisce la lista dei titoli dei progetti di ricerca il cui team è “coerente”, ossia
progetti in cui tutti gli scienziati coinvolti hanno l’ambito di ricerca del progetto tra i propri ambiti di interesse.
• scienziati_simili (self, nome_scienziato). Il metodo restituisce la lista dei nomi degli scienziati che hanno
partecipato a tutti i progetti di ricerca a cui ha partecipato lo scienziato il cui nome è passato come argomento.
TUTTE LE LISTE PRESENTI COME CAMPI DELLE CLASSI Scienziato, ProgettoDiRIcerca e Sistema, E TUTTE LE LISTE
SPECIFICATE COME OUTPUT DEI METODI SOPRA RICHIESTI SONO ISTANZE DELLA CLASSE ListaConcatenata
SVILUPPATA DURANTE IL CORSO.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Scienziato:
    def __init__(self, nome, listaRicerca):
        self.nome=nome
        self.listaRicerca=listaRicerca

    def __repr__(self):
        return f'Scienziato: {self.nome} - Lista ambito di ricerca: {self.listaRicerca}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Scienziato):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi accessori:

    def get_nome(self):
        return self.nome

    def get_ambiti_ricerca(self):
        return self.listaRicerca

class ProgettoDiRicerca:
    def __init__(self, titolo, listaTeam, listaContributi, ambitoRicerca):
        self.titolo=titolo
        self.listaTeam=listaTeam
        self.listaContributi=listaContributi
        self.ambitoRicerca=ambitoRicerca

    def __repr__(self):
        return f'ProgettoDiRicerca: {self.titolo} - Team di ricerca: {self.listaTeam}, Contributi del team: {self.listaContributi}, Ambito di ricerca: {self.ambitoRicerca}'

    def __eq__(self, other):
        if other is None or not isinstance(other, ProgettoDiRicerca):
            return False
        if other is self:
            return True
        return self.titolo==other.titolo

    #Metodi accessori:

    def get_titolo(self):
        return self.titolo

    def get_team(self):
        return self.listaTeam

    def get_contributi(self):
        return self.listaContributi

    def get_ambito_principale(self):
        return self.ambitoRicerca

class Sistema:
    def __init__(self, listaScienziati, listaProgetti):
        self.listaScienziati=listaScienziati
        self.listaProgetti=listaProgetti

    '''
    scienziato_max_contributo(self, amb). Il metodo restituisce il nome dello scienziato che ha fornito il massimo
    contributo complessivo in progetti di ricerca nell’ambito amb. Se più scienziati soddisfano la condizione, il
    metodo restituisce uno qualsiasi di essi
    '''
    def scienziato_max_contributo(self, amb):
        res = None
        d = {}
        iter_progetti = Iteratore(self.listaProgetti)
        while not iter_progetti.finito():
            progetto = next(iter_progetti)
            if progetto.get_ambito_principale() == amb:
                lista_scienziati = progetto.get_team()
                lista_contributi = progetto.get_contributi()
                iter_scienziati = Iteratore(lista_scienziati)
                iter_contributi = Iteratore(lista_contributi)
                while not iter_scienziati.finito() and not iter_contributi.finito():
                    scienziato = next(iter_scienziati)
                    contributo = next(iter_contributi)
                    d[scienziato] = d.get(scienziato, 0) + contributo
        max_contributo = -1
        for scienziato, contributo in d.items():
            if contributo > max_contributo:
                max_contributo = contributo
                res = scienziato.get_nome()
        return res
    
    '''
    team_coerente(self), che restituisce la lista dei titoli dei progetti di ricerca il cui team è “coerente”, ossia
    progetti in cui tutti gli scienziati coinvolti hanno l’ambito di ricerca del progetto tra i propri ambiti di interesse.
    '''
    def team_coerente(self):
        res = ListaConcatenata()
        iter_progetti = Iteratore(self.listaProgetti)
        while not iter_progetti.finito():
            progetto = next(iter_progetti)
            lista_scienziati = progetto.get_team()
            ambito_progetto = progetto.get_ambito_principale()
            iter_scienziati = Iteratore(lista_scienziati)
            team_coerente = True
            while not iter_scienziati.finito():
                scienziato = next(iter_scienziati)
                lista_ambiti_scienziato = scienziato.get_ambiti_ricerca()
                iter_ambiti_scienziato = Iteratore(lista_ambiti_scienziato)
                trovato = False
                while not iter_ambiti_scienziato.finito():
                    ambito = next(iter_ambiti_scienziato)
                    if ambito == ambito_progetto:
                        trovato = True
                        break
                if not trovato:
                    team_coerente = False
                    break
            if team_coerente:
                res.aggiungi_in_coda(progetto.get_titolo())
        return res
    
    '''
    scienziati_simili (self, nome_scienziato). Il metodo restituisce la lista dei nomi degli scienziati che hanno
    partecipato a tutti i progetti di ricerca a cui ha partecipato lo scienziato il cui nome è passato come argomento
    '''
    def scienziati_simili(self, nome_scienziato):
        res = ListaConcatenata()
        scienziato_ref = None
        iter_scienziati = Iteratore(self.listaScienziati)
        while not iter_scienziati.finito():
            scienziato = next(iter_scienziati)
            if scienziato.get_nome() == nome_scienziato:
                scienziato_ref = scienziato
                break
        set_scienziato_ref_progetti = set()
        iter_progetti = Iteratore(self.listaProgetti)
        while not iter_progetti.finito():
            progetto = next(iter_progetti)
            lista_scienziati = progetto.get_team()
            iter_scienziati_progetto = Iteratore(lista_scienziati)
            while not iter_scienziati_progetto.finito():
                s = next(iter_scienziati_progetto)
                if s == scienziato_ref:
                    set_scienziato_ref_progetti.add(progetto)
        iter_scienziati = Iteratore(self.listaScienziati)
        while not iter_scienziati.finito():
            scienziato = next(iter_scienziati)
            if scienziato == scienziato_ref:
                continue
            progetti_altro = set()
            iter_progetti = Iteratore(self.listaProgetti)
            while not iter_progetti.finito():
                progetto = next(iter_progetti)
                lista_team = progetto.get_team()
                iter_team = Iteratore(lista_team)
                while not iter_team.finito():
                    membro = next(iter_team)
                    if membro == scienziato:
                        progetti_altro.add(progetto)
                        break
            if set_scienziato_ref_progetti.issubset(progetti_altro):
                res.aggiungi_in_coda(scienziato.get_nome())
        return res



