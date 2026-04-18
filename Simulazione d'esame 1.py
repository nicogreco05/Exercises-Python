'''
30/05
Si implementi in Java una classe Sistema che fornisca metodi per l’analisi dei dati riguardanti articoli 
costruiti assemblando componenti. Si supponga che le classi Componente e Articolo siano già disponibili e forniscano i seguenti metodi: 
 
Classe Componente: 
public String getCodice(), che restituisce il codice che identifica il componente. 
public float getPrezzo(), che restituisce il prezzo di acquisto del componente. 
public boolean equals(Object o) 
public String toString() 
 
Classe Articolo: 
public String getNome(), che restituisce il nome che identifica l’articolo. 
public float getPrezzo(), che restituisce il prezzo di vendita dell’articolo. 
public LinkedList<String> getComponenti(), che restituisce la lista dei codici dei componenti utilizzati per la costruzione dell’articolo. 
public boolean equals(Object o) 
public String toString() 
 
Il profitto derivante da un articolo è dato dalla differenza tra il prezzo di vendita dell’articolo stesso e 
la somma dei prezzi dei suoi componenti. 
 
La classe Sistema contiene le liste dei componenti e degli articoli. 
Oltre ad eventuali metodi che si ritengano necessari, si includano almeno i seguenti metodi nella classe: 

public String articoloTop(). 
Il metodo restituisce il nome dell’articolo dal quale deriva il massimo profitto. 
Qualora la proprietà fosse soddisfatta da più articoli, il metodo restituisce uno qualsiasi di essi.

public LinkedList<String> componentiUniversali(). 
Il metodo restituisce la lista dei codici dei componenti utilizzati in tutti gli articoli. 

public LinkedList<String> articoliComponentiCostosi(float p). 
Il metodo restituisce la lista dei nomi degli articoli tra i cui componenti ne è presente almeno uno con prezzo maggiore di p. 
'''
from listaconcatenata import ListaConcatenata, Iteratore

class Componente:
    def __init__(self, codice : str, prezzo : float):
        self.codice = codice
        self.prezzo = prezzo
    def __eq__(self, other):
        return self.codice == other.codice
    def __repr__(self):
        return f'Componente({self.codice}, {self.prezzo})'
    def getCodice(self):
        return self.codice
    def getPrezzo(self):
        return self.prezzo

class Articolo:
    def __init__(self, nome : str, prezzo : float, componenti : ListaConcatenata):
        self.nome = nome
        self.prezzo = prezzo
        self.componenti = componenti
    def __eq__(self, other):
        return self.nome == other.nome
    def __repr__(self):
        return f'Articolo({self.nome}, {self.prezzo}, {self.componenti})'
    def getNome(self):
        return self.nome
    def getPrezzo(self):
        return self.prezzo
    def getComponenti(self):
        return self.componenti

class Sistema:
    def __init__(self, listaComponenti : list[Componente], listaArticoli : list[Articolo]):
        self.listaComponenti = listaComponenti
        self.listaArticoli = listaArticoli

    '''
    public String articoloTop(). 
    Il metodo restituisce il nome dell’articolo dal quale deriva il massimo profitto. 
    Qualora la proprietà fosse soddisfatta da più articoli, il metodo restituisce uno qualsiasi di essi.
    '''
    def _profitto(self, articolo):
        prezzo_vendita = articolo.getPrezzo()
        somma_prezzi_comp = 0
        iter_comp = Iteratore(articolo.getComponenti())
        while not iter_comp.finito():
            comp = next(iter_comp)
            for componente in self.listaComponenti:
                if componente.getCodice() == comp:
                    somma_prezzi_comp += componente.getPrezzo()
                    break
        return prezzo_vendita - somma_prezzi_comp
    
    def articoloTop(self):
        articolo_top = ""
        max_profitto = 0
        for articolo in self.listaArticoli:
            nome_articolo = articolo.getNome()
            profitto_articolo = self._profitto(articolo)
            if profitto_articolo > max_profitto:
                max_profitto = profitto_articolo
                articolo_top = nome_articolo
        return articolo_top




    '''
    public LinkedList<String> componentiUniversali(). 
    Il metodo restituisce la lista dei codici dei componenti utilizzati in tutti gli articoli. 
    '''
    def componentiUniversali(self):
      if not self.listaArticoli:
        return ListaConcatenata()
    # 1. Prendi i componenti del primo articolo come punto di partenza
      primo_articolo = self.listaArticoli[0]
      universali = set()
      iter_comp = Iteratore(primo_articolo.getComponenti())
      while not iter_comp.finito():
        universali.add(next(iter_comp))

    # 2. Fai l'intersezione con i componenti di ogni altro articolo
      for articolo in self.listaArticoli[1:]:
        temp = set()
        iter_comp = Iteratore(articolo.getComponenti())
        while not iter_comp.finito():
            temp.add(next(iter_comp))
        universali &= temp  # tieni solo quelli comuni

    # 3. Converti il risultato in ListaConcatenata
      res = ListaConcatenata()
      for comp in universali:
        res.aggiungi_in_coda(comp)
      return res
        
        
    '''
    public LinkedList<String> articoliComponentiCostosi(float p). 
    Il metodo restituisce la lista dei nomi degli articoli tra i cui componenti ne è presente almeno uno con prezzo maggiore di p. 
    '''
    def articoliComponentiCostosi(self, p):
        res = ListaConcatenata()
        for articolo in self.listaArticoli:
            trovato = False
            iter_comp = Iteratore(articolo.getComponenti())
            while not iter_comp.finito():
                componente = next(iter_comp)
                for componente in self.listaComponenti:
                    if componente.getCodice() == componente:
                        if componente.getPrezzo() > p:
                            trovato = True
                            break
                if trovato:
                    break
            if trovato:
                res.aggiungi_in_coda(articolo.getNome())
        return res


        




    