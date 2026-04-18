'''
Traccia 9 

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti giocatori e squadre. Si
supponga che siano definite le classi Giocatore e Squadra, che forniscono i seguenti metodi:
Classe Giocatore:
• get
_
nome (self), che restituisce il nome che identifica il giocatore.
• get
_
ruoli (self), che restituisce la lista dei ruoli in cui il giocatore è specializzato.
• get_numero_maglia (self), che restituisce il numero di maglia del giocatore.
•
__eq__(self, other).
• __repr__(self).
Classe Squadra:
• get
_
nome (self), che restituisce il nome della squadra.
• get
_
rosa (self), che restituisce la lista dei nomi dei giocatori che compongono la squadra.
• get_punteggi_ottenuti(self), che restituisce una lista di interi rappresentanti i punti ottenuti nelle ultime partite
disputate.
•
__eq__(self, other).
• __repr__(self).
La classe Sistema contiene le liste lista_giocatori dei giocatori e lista_squadre delle squadre. Oltre ad eventuali metodi
che si ritengano necessari, si includano almeno i seguenti metodi nella classe:
• giocatore_piu_vincente (self). Il metodo restituisce il nome del giocatore che milita nella squadra con la media
punti più alta. Se più giocatori soddisfano la condizione, il metodo ne restituisce uno qualsiasi.
• squadre_idonee_per_ruolo (self, ruolo). Il metodo restituisce la lista dei nomi delle squadre in cui almeno un
giocatore è specializzato nel ruolo passato come argomento.
• giocatori_fedeli (self, nome_squadra). Il metodo restituisce la lista dei nomi dei giocatori che appartengono
alla squadra con nome nome_squadra e che non hanno mai giocato in nessun'altra squadra presente nel
sistema.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Giocatore:
    def __init__(self, nome, listaRuoli, numMaglia):
        self.nome=nome
        self.listaRuoli=listaRuoli
        self.numMaglia=numMaglia

    def __repr__(self):
        return f'Giocatore: {self.nome} - Ruoli preferiti: {self.listaRuoli}, Numero maglia: {self.numMaglia}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Giocatore):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi accessori:

    def get_nome(self):
        return self.nome

    def get_ruoli(self):
        return self.listaRuoli

    def get_numero_maglia(self):
        return self.numMaglia

class Squadra:
    def __init__(self, nome, listaRosa, listaPunti):
        self.nome=nome
        self.listaRosa=listaRosa
        self.listaPunti=listaPunti

    def __repr__(self):
        return f'Squadra: {self.nome} - Rosa squadra: {self.listaRosa}, Storico punti: {self.listaPunti}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Squadra):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi accessori:

    def get_nome(self):
        return self.nome

    def get_rosa(self):
        return self.listaRosa

    def get_punteggi_ottenuti(self):
        return self.listaPunti

class Sistema:
    def __init__(self, listaGiocatori, listaSquadre):
        self.listaGiocatori=listaGiocatori
        self.listaSquadre=listaSquadre

    '''
    giocatore_piu_vincente (self). Il metodo restituisce il nome del giocatore che milita nella squadra con la media
    punti più alta. Se più giocatori soddisfano la condizione, il metodo ne restituisce uno qualsiasi.
    '''
    def giocatore_piu_vincente(self):
        res = None
        max_media = -1
        iter_giocatori = Iteratore(self.listaGiocatori)
        while not iter_giocatori.finito():
            giocatore = next(iter_giocatori)
            iter_squadre = Iteratore(self.listaSquadre)
            while not iter_squadre.finito():
                squadra = next(iter_squadre)
                lista_gioc = squadra.get_rosa()
                punteggi = squadra.get_punteggi_ottenuti()
                punteggio_tot = 0
                count = 0
                if giocatore.get_nome() in lista_gioc:
                    for punteggio in punteggi:
                        punteggi += punteggio
                        count += 1
            media = punteggio_tot / count
            if media > max_media:
                max_media = media
                res = giocatore.get_nome()
        return res
