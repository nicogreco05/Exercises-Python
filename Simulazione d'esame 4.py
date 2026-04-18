'''
11/06

Si implementi in Java una classe Sistema che fornisca metodi per l'analisi di dati relativi a prenotazioni di voli gestiti da una compagnia aerea. Si supponga che le classi Volo e Prenotazione siano già disponibili e forniscano i seguenti metodi:
Classe Volo:
• public String getPartenza(), che restituisce il nome dell'aeroporto di partenza del volo.
public String getArrivo(), che restituisce il nome dell'aeroporto di arrivo del volo.
public int getPrezzoBusiness(), che restituisce il prezzo di un posto in classe business.
• public int getPrezzoEconomica(), che restituisce il prezzo di un posto in classe economica.
• public boolean equals(Object o).
• public String toString().
Classe Prenotazione:
• public LinkedList«String> getPercorso(), che restituisce il percorso per cui è stata effettuata la prenotazioni cioè la lista dei nomi degli aeroporti attraversati. Ovviamente, o il primo aeroporto nel percorso è quello di partenza;
• l'ultimo aeroporto nel percorso è quello di destinazione;
• un aeroporto compare al più una volta nel percorso;
ogni coppia consecutiva di aeroporti nel percorso corrisponde ad un singolo volo.
public String getNomeCliente(), che restituisce il nome del cliente che ha effettuato la prenotazione.
• public String getClasse(), che restituisce la classe del posto prenotato ("business" o "economica").
• public boolean equals(Object o).
• public String toString().
La classe Sistema contiene le liste dei voli e delle prenotazioni effettuate. Oltre ad eventuali metodi che si ritengano utili, si includano nella classe almeno i seguenti metodi:
• public boolean verificaPrenotazioni(). Il metodo restituisce true se e solo se tutte le prenotazioni sono corrette.
Una prenotazione è corretta se esiste un volo per ogni coppia consecutiva di aeroporti nel percorso prenotato.
• public Volo voloMax(). Il metodo restituisce il volo per il quale è stata incassata la somma maggiore. Nel caso in cui più voli soddisfino la proprietà, il metodo restituisce uno qualsiasi di essi.
L'incasso di un volo è dato dalla formula
PrenBusiness x prezzoBusiness + nPrenEconomica x prezzoEconomica
dove PrenBusiness e PrenEconomica sono i numeri di prenotazioni in classe economica e business effettuate per il volo, mentre prezzoBusiness e prezzoEconomica sono i prezzi del volo in ciascuna delle due classi.
• public LinkedList<String> destinazioneComune(String cliente). Il metodo restituisce la lista dei nomi dei clienti che hanno almeno una destinazione in comune con il cliente cliente, cioè i clienti che hanno effettuato almeno una prenotazione avente come destinazione una delle destinazioni presenti nelle prenotazioni effettuate dal
cliente cliente.
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Volo:
    def __init__(self, partenza, arrivo, prezzoBusiness, prezzoEconomica):
        self.partenza = partenza
        self.arrivo = arrivo
        self.prezzoBusiness = prezzoBusiness
        self.prezzoEconomica = prezzoEconomica
    def getPartenza(self):
        return self.partenza
    def getArrivo(self):
        return self.arrivo
    def getPrezzoBusiness(self):
        return self.prezzoBusiness
    def getPrezzoEconomica(self):
        return self.prezzoEconomica
    def __eq__(self, other):
        return self.partenza == other.partenza and self.arrivo == other.arrivo
    def __repr__(self):
       return "Partenza: "+ self.partenza + " Arrivo: "+ self.arrivo
    def __hash__(self):
        return hash((self.partenza, self.arrivo, self.prezzoBusiness, self.prezzoEconomica))

class Prenotazione:
    def __init__(self, percorso : ListaConcatenata, nomeCliente, classe):
        self.percorso = percorso
        self.nomeCliente = nomeCliente
        self.classe = classe
    def getPercorso(self):
        return self.percorso
    def getNomeCliente(self):
        return self.nomeCliente
    def getClasse(self):
        return self.classe
    def __eq__(self, other):
        return self.percorso == other.percorso and self.nomeCliente == other.nomeCliente
    def __repr__(self):
        return "Percorso: "+ self.percorso


class Sistema:
    def __init__(self, voli : list[Volo], prenotazioni : list[Prenotazione]):
        self.voli = voli
        self.prenotazioni = prenotazioni

    '''
    • public boolean verificaPrenotazioni(). Il metodo restituisce true se e solo se tutte le prenotazioni sono corrette.
    Una prenotazione è corretta se esiste un volo per ogni coppia consecutiva di aeroporti nel percorso prenotato.
    '''
    def verficaPrenotazioni(self):
        for prenotazione in self.prenotazioni:
            percorso = prenotazione.getPercorso()
            iter_percorso = Iteratore(percorso)
            if iter_percorso.finito():
                continue
            partenza = next(iter_percorso)
            while not iter_percorso.finito():
                arrivo = next(iter_percorso)
                volo_valido = False
                for volo in self.voli:
                    if volo.getPartenza() == partenza and volo.getArrivo == arrivo:
                        volo_valido = True
                        break
                if not volo_valido:
                    return False
                partenza = arrivo
        return True
    
    '''
    • public Volo voloMax(). Il metodo restituisce il volo per il quale è stata incassata la somma maggiore. 
    Nel caso in cui più voli soddisfino la proprietà, il metodo restituisce uno qualsiasi di essi.
    L'incasso di un volo è dato dalla formula
    PrenBusiness x prezzoBusiness + nPrenEconomica x prezzoEconomica
    dove PrenBusiness e PrenEconomica sono i numeri di prenotazioni in classe economica e business effettuate per il volo, 
    mentre prezzoBusiness e prezzoEconomica sono i prezzi del volo in ciascuna delle due classi.
    '''
    def voloMax(self):
        incassi = {}
        for volo in self.voli:
            incassi[volo] = 0
        for prenotazione in self.prenotazioni:
            percorso = prenotazione.getPercorso()
            classe = prenotazione.getClasse()
            iter_percorso = Iteratore(percorso)
            partenza = next(percorso)
            while not iter_percorso.finito():
                arrivo = next(iter_percorso)
                for volo in self.voli:
                    if volo.getArrivo == arrivo and volo.getPartenza == partenza:
                        if classe == "businnes":
                            incassi[volo] += volo.getPrezzoBusiness()
                        else:
                            incassi[volo] += volo.getPrezzoEconomica()
                        break
                partenza = arrivo
        volo_max = None
        prezzo_max = -1
        for volo, prezzo in incassi.items():
            if prezzo > prezzo_max:
                prezzo_max = prezzo
                volo_max = volo
        return volo
    
    '''
    • public LinkedList<String> destinazioneComune(String cliente). 
    Il metodo restituisce la lista dei nomi dei clienti che hanno almeno una destinazione in comune 
    con il cliente cliente, cioè i clienti che hanno effettuato almeno una prenotazione avente come destinazione u
    na delle destinazioni presenti nelle prenotazioni effettuate dal
    cliente cliente.
    '''
    def destinazioneComune(self, cliente):
        res = ListaConcatenata()
        dest_cliente = set()
        for prenotazione in self.prenotazioni:
            if prenotazione.getNomeCliente == cliente:
                percorso = prenotazione.getPercorso()
                iter_percorso = Iteratore(percorso)
                ultima_dest = None
                while not iter_percorso.finito():
                    ultima_dest = next(iter_percorso)
                prenotazione.add(ultima_dest)
        des_altro_cliente = set()
        for prenotazione in self.prenotazioni:
            nome_cliente = prenotazione.getNomeCliente()
            if nome_cliente != cliente:
                percorso = prenotazione.getPercorso()
                iter_percorso = Iteratore(percorso)
                last_dest = None
                while not iter_percorso.finito():
                    last_dest = next(iter_percorso)
                if last_dest in dest_cliente:
                    des_altro_cliente.add(nome_cliente)
        for c in des_altro_cliente:
            res.aggiungi_in_coda(c)
        return res

        




        
