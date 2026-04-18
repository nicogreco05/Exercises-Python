'''
03/06
Si implementi in Java una classe Torneo che fornisca metodi per l’analisi dei dati riguardanti un torneo di calcio. Si supponga che siano già disponibili le classi Squadra e Partita, e che queste forniscano i seguenti metodi: 
 
Classe Squadra: 
public String getNome(), che restituisce il nome che identifica la squadra. 
public String getCitta(), che restituisce la città della squadra. 
public boolean equals(Object o). 
public String toString(). 
 
Classe Partita: 
public String getNomeSquadraInCasa(), che restituisce il nome della squadra che ha giocato la partita in casa. 
public String getNomeSquadraOspite(), che restituisce il nome della squadra che ha giocato la partita fuori casa. 
public int getGoalSquadraInCasa(), che restituisce il numero di goal segnati dalla squadra di casa. 
public int getGoalSquadraOspite(), che restituisce il numero di goal segnati dalla squadra ospite. 
public String getNomeArbitro(), che restituisce il nome dell’arbitro che ha arbitrato la partita. 
public String getCittaArbitro(), che restituisce la città dell’arbitro che ha arbitrato la partita. 
public boolean equals(Object o). 
public String toString(). 
 
NON È NECESSARIO IMPLEMENTARE ALCUNO DEI METODI SOPRA RIPORTATI. 
 
La classe Torneo contiene le liste delle squadre e delle partite. 
Tali liste devono essere implementate utilizzando la classe LinkedList. 
Oltre ad eventuali metodi che si ritengano necessari, si includano almeno i seguenti metodi nella classe: 

public LinkedList<String> squadreCasalinghe(). Il metodo restituisce la lista dei nomi delle squadre che hanno conseguito il maggior numero di vittorie nelle partite disputate in casa. 
public LinkedList<String> arbitriFuoriCItta(). Il metodo restituisce la lista dei nomi degli arbitri tali che tutte le partite da essi arbitrate non si sono svolte nella loro città (si noti che la città in cui si è svolta una partita è la città della squadra di casa). 
public LinkedList<String> arbitri3squadre(). Il metodo restituisce la lista dei nomi degli arbitri tali che l’insieme delle squadre distinte da essi arbitrate ha cardinalità 3 (si intende che un arbitro ha arbitrato una squadra se egli ha arbitrato una partita in cui tale squadra ha partecipato come squadra di casa o ospite). 
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Squadra:
    def __init__(self, nome, citta):
        self.nome = nome
        self.citta = citta
    def getNome(self):
        return self.nome
    def getCitta(self):
        return self.citta
    def __eq__(self, other):
        return self.nome == other.nome
    def __repr__(self):
        return "Squadra(%r, %r)" % (self.nome, self.citta)

class Partita:
    def __init__(self, nomeSquadraInCasa, nomeSquadraOspite,
                 goalSquadraInCasa, goalSquadraOspite, nomeArbitro, cittaArbitro):
        self.nomeSquadraInCasa = nomeSquadraInCasa
        self.nomeSquadraOspite = nomeSquadraOspite
        self.goalSquadraInCasa = goalSquadraInCasa
        self.goalSquadraOspite = goalSquadraOspite
        self.nomeArbitro = nomeArbitro
        self.cittaArbitro = cittaArbitro

    def getNomeSquadraInCasa(self):
        return self.nomeSquadraInCasa
    def getNomeSquadraOspite(self):
        return self.nomeSquadraOspite
    def getGoalSquadraInCasa(self):
        return self.goalSquadraInCasa
    def getGoalSquadraOspite(self):
        return self.goalSquadraOspite
    def getNomeArbitro(self):
        return self.nomeArbitro
    def getCittaArbitro(self):
        return self.cittaArbitro

    def __eq__(self, other):
        return (self.goalSquadraInCasa == other.goalSquadraInCasa and self.goalSquadraOspite
                == other.goalSquadraOspite and self.nomeArbitro
                == other.nomeArbitro and self.cittaArbitro ==
                other.cittaArbitro and self.nomeSquadraInCasa == other.nomeSquadraInCasa and
                self.nomeSquadraOspite == other.nomeSquadraOspite)
    def __repr__(self):
        return "Partita (%r,%r)" % (self.nomeSquadraInCasa, self.nomeSquadraOspite)


class Torneo:
    def __init__(self, squadre : list[Squadra], partite : list[Partita]):
        self.squadre = squadre
        self.partite = partite

    '''
    public LinkedList<String> squadreCasalinghe(). 
    Il metodo restituisce la lista dei nomi delle squadre che hanno conseguito il maggior numero 
    di vittorie nelle partite disputate in casa. 
    '''
    def squadreCasalinghe(self):
        res = ListaConcatenata()
        vittorie = {}
        for partita in self.partite:
            squadra_casa = partita.getNomeSquadraInCasa()
            gol_casa = partita.getGoalSquadraInCasa()
            gol_ospite = partita.getGoalSquadraOspite()
            if gol_casa > gol_ospite:
                vittorie[squadra_casa] = vittorie.get(squadra_casa, 0) + 1 # cerco nel dizionario vittorie la squadra casa, se ce prende il valore (ovvero le vittorie) e gli aggiunge 1 altrimento inizializza a 0 e aggiunge 1
        max_vittorie = max(vittorie.values()) # prende il massimo nel dizionario vittore  (.values per prendere i valori numerici)
        res = ListaConcatenata()
        for squadra, n_vittorie in vittorie.items(): # .items per accedere sia alla chiave (nome squadra) che al valore (n_vittorie)
            if n_vittorie == max_vittorie:
                res.aggiungi_in_coda(squadra)
        return res
    
    '''
    public LinkedList<String> arbitriFuoriCItta(). 
    Il metodo restituisce la lista dei nomi degli arbitri tali che tutte le partite da essi arbitrate non si sono svolte nella 
    loro città (si noti che la città in cui si è svolta una partita è la città della squadra di casa). 
    '''
    def arbitriFuoriCitta(self):
        res = ListaConcatenata()
        arbitraggio_locale = {}
        for partita in self.partite:
            arbitro = partita.getNomeArbitro()
            citta_arbitro = partita.getCittaArbitro()
            squadra_casa = partita.getNomeSquadraInCasa()
            citta_partita = None
            for squadra in self.squadre:
                if squadra.getNome() == squadra_casa:
                    citta_partita = squadra.getCitta()
                    break
            if arbitro not in arbitraggio_locale: # se non è nel dizionario lo aggiungo e gli assegno false 
                arbitraggio_locale[arbitro] = False
            if citta_arbitro == citta_partita: # altrimenti se le citta sono uguali aggiorno a true poiche ha arbitrato nella stessa citta
                arbitraggio_locale[arbitro] = True
        for arbitro, ha_arbitrato_nella_sua_citta in arbitraggio_locale.items():
            if not ha_arbitrato_nella_sua_citta:
                res.aggiungi_in_coda(arbitro)
        return res
            

    
    '''
    public LinkedList<String> arbitri3squadre(). 
    Il metodo restituisce la lista dei nomi degli arbitri tali che l’insieme delle squadre distinte da essi arbitrate 
    ha cardinalità 3 (si intende che un arbitro ha arbitrato una squadra se egli ha arbitrato una partita in cui tale 
    squadra ha partecipato come squadra di casa o ospite). 
    '''
    def arbitri3squadre(self):
        res = ListaConcatenata()
        arbitri_squadre = {} # dizionario: chiave --> arbitro il quale ha arbitrato tot squadre
        for partita in self.partite:
            squadra_casa = partita.getNomeSquadraInCasa()
            squadra_ospite = partita.getNomeSquadraOspite()
            arbitro = partita.getNomeArbitro()
            if arbitro not in arbitri_squadre: # se l'arbitro in questine non è nel dizionario allora...
                arbitri_squadre[arbitro] = set() # ...lo aggiungo e gli do un set vuoto
            # aggiungo le squadre (grazie al set non aggiungero i duplicati)
            arbitri_squadre[arbitro].add(squadra_casa) 
            arbitri_squadre[arbitro].add(squadra_ospite)
        for arbitro, squadre in arbitri_squadre.items(): # ciclo per ogni elemento del dizionario
            if len(squadre) == 3:
                res.aggiungi_in_coda(arbitro)
        return res



