'''
Traccia 4

Si implementi in Python una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti prenotazioni di servizi
da parte di clienti. Si supponga che siano definite le classi Prenotazione e Cliente, che forniscono i seguenti metodi:
Classe Prenotazione:
• get_codice(self), che restituisce il codice che identifica la prenotazione.
• get_clienti(self), che restituisce la lista dei nomi dei clienti che hanno effettuato la prenotazione.
• get_servizi_prenotati(self), che restituisce la lista dei servizi prenotati.
• get_data(self), che restituisce la data (espressa mediante un intero) in cui è stata effettuata la prenotazione.
• __eq__(self, other).
• __repr__(self).
Classe Cliente:
• get_nome(), che restituisce il nome che identifica il cliente.
• get_servizi_preferiti(), che restituisce la lista dei servizi preferiti dal cliente.
• __eq__(self, other).
• __repr__(self).
La classe Sistema contiene le liste lista_prenotazioni delle prenotazioni e lista_clienti dei clienti. Oltre ad eventuali
metodi che si ritengano necessari, si includano almeno i seguenti metodi nella classe Sistema:
• seleziona_cliente(self, codice_pren), che restituisce il nome del cliente c che soddisfa entrambe le seguenti
condizioni:
• il cliente c ha effettuato la prenotazione con codice codice_pren;
• non esiste nessun altro cliente che ha effettuato la prenotazione con codice codice_pren ed ha un
servizio preferito in comune con il cliente c.
Se più clienti soddisfano le condizioni, il metodo restituisce uno qualsiasi di essi.
• servizio_frequente(self, d). Il metodo restituisce il servizio che è stato prenotato il maggior numero di volte in
date successive a d. Se più servizi soddisfano la condizione, il metodo restituisce uno qualsiasi di essi.
• servizi_essenziali(self, nome_cliente). Il metodo restituisce la lista dei servizi preferiti dal cliente di nome
nome_cliente che sono stati prenotati in tutte le prenotazioni effettuate dal cliente stesso.
'''
from listaconcatenata import ListaConcatenata

class Prenotazione:
    def __init__(self, codice, listaClienti, listaServizi, data):
        self.codice=codice
        self.listaClienti=listaClienti
        self.listaServizi=listaServizi
        self.data=data

    def __repr__(self):
        return f'Prenotazione: {self.codice} - {self.destinazione} Clienti: {self.listaClienti}, Servizi prenotati: {self.listaServizi}, In data: {self.data}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Prenotazione):
            return False
        if other is self:
            return True
        return self.codice==other.codice

    #Metodi richiesti:

    def get_codice(self):
        return self.codice

    def get_clienti(self):
        return self.listaClienti

    def get_servizi_prenotati(self):
        return self.listaServizi

    def get_data(self):
        return self.data

class Cliente:
    def __init__(self, nome, listaPreferiti):
        self.nome=nome
        self.listaPreferiti=listaPreferiti

    def __repr__(self):
        return f'Cliente: {self.nome} - {self.destinazione} Servizi preferiti: {self.listaPreferiti}'

    def __eq__(self, other):
        if other is None or not isinstance(other, Cliente):
            return False
        if other is self:
            return True
        return self.nome==other.nome

    #Metodi richiesti:

    def get_nome(self):
        return self.nome

    def get_servizi_preferiti(self):
        return self.listaPreferiti


class Sistema:
    def __init__(self, listaPrenotazioni, listaClienti):
        self.listaPrenotazioni=listaPrenotazioni
        self.listaClienti=listaClienti

    '''
    • seleziona_cliente(self, codice_pren), che restituisce il nome del cliente c che soddisfa entrambe le seguenti
    condizioni:
    • il cliente c ha effettuato la prenotazione con codice codice_pren;
    • non esiste nessun altro cliente che ha effettuato la prenotazione con codice codice_pren ed ha un
    servizio preferito in comune con il cliente c.
    '''
    def selezione_cliente(self, codice_pren):
        for prenotazione in self.listaPrenotazioni:
            if prenotazione.get_codice() == codice_pren:
                lista_clienti = prenotazione.get_clienti()
                for cliente1 in lista_clienti:
                    servizi_pref = set(cliente1.get_servizi_preferiti())
                    comune_trovato = False
                    for cliente2 in lista_clienti:
                        servizi_pref_2 = set(cliente2.get_servizi_preferiti())
                        if servizi_pref.intersection(servizi_pref_2):
                            comune_trovato = True
                    if not comune_trovato:
                        return cliente1.get_nome()
        return -1
    
    '''
    • servizio_frequente(self, d). Il metodo restituisce il servizio che è stato prenotato il maggior numero di volte in
    date successive a d. Se più servizi soddisfano la condizione, il metodo restituisce uno qualsiasi di essi.
    '''
    def servizio_frequente(self, d):
        res = None
        dict = {}
        for prenotazione in self.listaPrenotazioni:
            if prenotazione.get_data() > d:
                for servizio in prenotazione.get_servizi_prenotati():
                    dict[servizio] = dict.get(servizio, 0) + 1
        max_count = 0
        for servizio, count in dict.items():
            if count > max_count:
                max_count = count
                res = servizio
        return res
        
    '''
    • servizi_essenziali(self, nome_cliente). Il metodo restituisce la lista dei servizi preferiti dal cliente di nome
    nome_cliente che sono stati prenotati in tutte le prenotazioni effettuate dal cliente stesso.
    '''
    def servizi_essenziali(self, nome_cliente):
        cliente_ref = None
        for cliente in self.listaClienti:
            if cliente.get_nome() == nome_cliente:
                cliente_ref = cliente
        servizi_pref = set(cliente_ref.get_servizi_preferiti())
        altri_serivizi = set()
        for prenotazione in self.listaPrenotazioni:
            if cliente_ref in prenotazione.get_clienti():
                altri_serivizi.update(prenotazione.get_servizi_prenotati())
        res = servizi_pref.intersection(altri_serivizi)
        return res
                        

                    
