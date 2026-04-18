'''
Traccia 5

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti studenti, corsi
frequentati e valutazioni ottenute. Si supponga che siano definite le classi Studente e Corso, che forniscono i seguenti
metodi:
Classe Studente:
• get
_
matricola (self), che restituisce la matricola che identifica lo studente.
• get_nome (self), che restituisce il nome dello studente.
• get_corsi (self), che restituisce una lista dei codici dei corsi frequentati dallo studente.
•
__eq__(self, other).
• __repr__(self).
Classe Corso:
• get_codice(self), che restituisce il codice che identifica il corso.
• get_nome (self), che restituisce il nome del corso.
• get
_
valutazioni (self), che restituisce una lista di tuple (matricola, voto).
•
__eq__(self, other).
• __repr__(self).
La classe Sistema contiene le liste lista
studenti di studenti e lista
_
_
ritengano necessari, si includano almeno i seguenti metodi nella classe:
corsi dei corsi. Oltre ad eventuali metodi che si
• promossi_in_tutti(self, soglia): restituisce una lista di nomi degli studenti che hanno superato con un voto
almeno pari a soglia tutti i corsi a cui sono iscritti.
• corso_con_media_massima(self): restituisce il nome del corso con la media più alta tra i voti assegnati. In caso
di parità, si può restituire un corso qualsiasi.
• studenti_non_comuni(self, codice_corso): restituisce una lista dei nomi degli studenti che non condividono
alcun corso con gli studenti iscritti al corso con codice codice_corso.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Studente:
    def __init__(self, matricola, nome, listaCorsi):
        self.matricola=matricola
        self.nome=nome
        self.listaCorsi=listaCorsi

    def __repr__(self):
        return f'Studente: {self.matricola} - {self.nome}, Corsi: {self.listaCorsi}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Studente):
            return False
        if other is self:
            return True
        return self.matricola==other.matricola

    #Metodi accessori:

    def get_matricola(self):
        return self.matricola

    def get_nome(self):
        return self.nome

    def get_corsi(self):
        return self.listaCorsi

class Corso:
    def __init__(self, codice, nome, valutazioni):
        self.codice=codice
        self.nome=nome
        self.valutazioni=valutazioni

    def __repr__(self):
        return f'Corso: {self.codice} - {self.nome}, Valutazioni: {self.valutazioni}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Corso):
            return False
        if other is self:
            return True
        return self.codice==other.codice

    #Metodi accessori:

    def get_codice(self):
        return self.codice

    def get_nome(self):
        return self.nome

    def get_valutazioni(self):
        return self.valutazioni

class Sistema:
    def __init__(self, listaStudenti, listaCorsi):
        self.listaStudenti=listaStudenti
        self.listaCorsi=listaCorsi

    '''
    promossi_in_tutti(self, soglia): restituisce una lista di nomi degli studenti che hanno superato con un voto
    almeno pari a soglia tutti i corsi a cui sono iscritti.
    '''
    def promossi_in_tutti(self, soglia):
        res = ListaConcatenata()
        iter_studenti = Iteratore(self.listaStudenti)
        while not iter_studenti.finito():
            studente = next(iter_studenti)
            lista_corsi = studente.get_corsi()
            iter_lista_corsi = Iteratore(lista_corsi)
            tutti_superati = True
            while not iter_lista_corsi.finito():
                corso = next(iter_lista_corsi)
                superato = True
                iter_corsi = Iteratore(self.listaCorsi)
                while not iter_corsi.finito():
                    c = next(iter_corsi)
                    if corso.get_codice() == c.get_codice():
                        lista_valutazioni = c.get_valutazioni()
                        voto_studente = None
                        for matricola, voto in lista_valutazioni:
                            if matricola == studente.get_matricola():
                                voto_studente = voto
                                if voto_studente < soglia:
                                    superato = False
                if not superato:
                    tutti_superati = False
            if tutti_superati:
                res.aggiungi_in_coda(studente.get_nome())
        return res
    
    '''
    corso_con_media_massima(self): restituisce il nome del corso con la media più alta tra i voti assegnati. In caso
    di parità, si può restituire un corso qualsiasi
    '''
    def corso_con_media_massima(self):
        res = None
        max_media = -1
        iter_corsi = Iteratore(self.listaCorsi)
        while not iter_corsi.finito():
            corso = next(iter_corsi)
            lista_valutazioni = corso.get_valutazioni()
            somma = 0
            count = 0
            for matricola, voti in lista_valutazioni:
                somma += voti
                count += 1
            media = somma / count
            if media > max_media:
                max_media = media
                res = corso.get_nome()
        return res
