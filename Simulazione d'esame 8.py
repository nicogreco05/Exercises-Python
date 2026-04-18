'''
26/06

Si vuole implementare in Java un sistema che supporti la Pubblica Amministrazione nella gestione di proprietà immobiliari, ad esempio per il calcolo di alcune tasse. Il sistema gestisce informazioni su immobili (istanze della classe Immobile), su persone (istanze della classe Persona) e su proprietà (istanze della classe Proprietà), che collegano le persone agli immobili da esse possedute, con una certa quota percentuale di proprietà. 
Ogni Persona è identificata da un codice fiscale ed è caratterizzata dall’indirizzo di residenza, costituito dalla via e dalla città in cui quella persona risiede. 
Un Immobile è identificato da un codice catastale ed è caratterizzato dall’indirizzo, costituito dalla via e dalla città in cui è ubicato, dalla dimensione in metri quadrati, dal valore catastale e da una lista di proprietà, che specifica i proprietari di quell’immobile. 
Ciascun oggetto della classe Proprietà è identificato dal codice fiscale del proprietario ed è caratterizzato dal codice catastale dell’immobile e dalla percentuale di possesso (espressa come valore compreso tra 0 ed 1). 
 
Si implementino in Java le classi Immobile, Persona e Proprietà. Si implementi inoltre la classe Sistema, scegliendo opportunamente le classi Java più adeguate per gestire le informazioni sulle varie persone e sugli immobili.  
Oltre a scrivere eventuali metodi che si ritengono necessari per implementare l’applicazione, occorre fornire almeno i seguenti metodi nella classe Sistema: 
 
public ArrayList<Persona> contribuenti (String c). Il metodo restituisce l’elenco di tutte le persone che possiedono immobili ubicati nella città c. 
public ArrayList<Immobile> piuProprietari(). Il metodo restituisce l’elenco degli immobili di proprietà di più persone, tali che solo una di esse risiede allo stesso indirizzo in cui è ubicato l’immobile. 
public ArrayList<String> grandiProprieta(String c, int d). Il metodo restituisce la lista dei codici fiscali delle persone residenti nella città c che posseggono immobili di dimensione almeno d, ordinata in base alla via di residenza delle persone stesse (secondo l’ordine lessicografico). 
public HashMap<Persona, Double> patrimoni(String c). Il metodo restituisce una HashMap in cui, per ogni persona residente nella città c, è riportato il valore totale del patrimonio immobiliare posseduto. Si noti che per il calcolo di tale valore occorre tener conto della percentuale di possesso dei vari immobili di quella persona: se possiede un immobile di valore x con percentuale di possesso p, il valore patrimoniale da considerare per tale immobile sarà v = x * p. 
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Persona:
    def __init__(self, cf, via, citta):
        self._cf = cf
        self._via = via
        self._citta = citta
    def __eq__(self, other):
        return self._cf == other._cf
    def getCf(self):
        return self._cf
    def getVia(self):
        return self._via
    def getCitta(self):
        return self._citta
    def __repr__(self):
        return self._cf

class Immobile:
    def __init__(self, codice, via, citta, dimensioni, valore, proprietari : ListaConcatenata):
        self._codice = codice
        self._via = via
        self._citta = citta
        self._dimensioni = dimensioni
        self._valore = valore
        self._proprietari = proprietari
    def __eq__(self, other):
        return self._codice == other._codice
    def getCodice(self):
        return self._codice
    def getVia(self):
        return self._via
    def getCitta(self):
        return self._citta
    def getDimensioni(self):
        return self._dimensioni
    def getValore(self):
        return self._valore
    def getProprietari(self):
        return self._proprietari
    def __repr__(self):
        return self._codice

class Proprieta:
    def __init__(self, cf, codice, possesso):
        self._cf = cf
        self._codice = codice
        self._possesso = possesso
    def __eq__(self, other):
        return self._cf == other._cf and self._codice == other.codice
    def getCf(self):
        return self._cf
    def getCodice(self):
        return self._codice
    def getPossesso(self):
        return self._possesso
    def __repr__(self):
        return self._cf

class Sistema:
    def __init__(self, persone : list[Persona], immobili : list[Immobile], proprieta: list[Proprieta]):
        self._persone = persone
        self._immobili = immobili
        self._proprieta = proprieta

    '''
    public ArrayList<Persona> contribuenti (String c). 
    Il metodo restituisce l’elenco di tutte le persone che possiedono immobili ubicati nella città c. 
    '''
    def contribuenti(self, c):
        res = ListaConcatenata()
        for immobile in self._immobili:
            if immobile.getCitta() == c:
                proprietari = immobile.getProprietari()
                iter_proprietari = Iteratore(proprietari)
                while not iter_proprietari.finito():
                    proprietario = next(iter_proprietari)
                    res.aggiungi_in_coda(proprietario)
        return res
    
    '''
    public ArrayList<Immobile> piuProprietari(). 
    Il metodo restituisce l’elenco degli immobili di proprietà di più persone, tali che solo una di esse 
    risiede allo stesso indirizzo in cui è ubicato l’immobile. 
    '''
    def piuProprietari(self):
        res = ListaConcatenata()
        for immobile in self._immobili:
            propietari = immobile.getProprietari()
            if len(propietari) > 1:
                via_immobile = immobile.getVia()
                citta_immbolie = immobile.getCitta()
                iter_proprietari = Iteratore(propietari)
                count_stessa_residenza = 0
                while not iter_proprietari.finito():
                    propietario = next(iter_proprietari)
                    if propietario.getVia() == via_immobile and propietario.getCitta() == citta_immbolie:
                        count_stessa_residenza += 1
                if count_stessa_residenza == 1:
                    res.aggiungi_in_coda(immobile)
        return res
    
    '''
    public ArrayList<String> grandiProprieta(String c, int d). 
    Il metodo restituisce la lista dei codici fiscali delle persone residenti nella città c che posseggono immobili 
    di dimensione almeno d, ordinata in base alla via di residenza delle persone stesse (secondo l’ordine lessicografico). 
    '''
    def grandiProprieta(self, c, d):
        lista = []
        for immobile in self._immobili:
            if immobile.getDimensioni() >= d:
                proprietari = immobile.getProprietari()
                iter_propr = Iteratore(proprietari)
                while not iter_propr.finito():
                    persona = next(iter_propr)
                    if persona.getCitta() == c:
                        lista.append(persona)
        lista.sort(key = lambda p:p.getVia())
        res = ListaConcatenata()
        for persona in lista:
            res.aggiungi_in_coda(persona.getCf())
        return res
    
    '''
    public HashMap<Persona, Double> patrimoni(String c). 
    Il metodo restituisce una HashMap in cui, per ogni persona residente nella città c,
    è riportato il valore totale del patrimonio immobiliare posseduto. Si noti che per il calcolo di 
    tale valore occorre tener conto della percentuale di possesso dei vari immobili di quella persona: 
    se possiede un immobile di valore x con percentuale di possesso p, il valore patrimoniale da considerare 
    per tale immobile sarà v = x * p. 
    '''
    def patrimoni(self, c):
        res = {}
        for persona in self._persone:
            if persona.getCitta() == c:
                cf_persona = persona.getCf()
                patrimonio = 0.0
                for proprieta in self._proprieta:
                    if proprieta.getCf() == cf_persona:
                        codice_immobile = proprieta.getCodice()
                        perc_possesso = proprieta.getPossesso()
                        for immobile in self._immobili:
                            if immobile.getCodice() == codice_immobile:
                                valore = immobile.getValore()
                                patrimonio += valore * perc_possesso
                if patrimonio > 0:
                    res[persona] = patrimonio
        return res



                