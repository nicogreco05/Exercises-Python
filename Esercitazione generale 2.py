'''
Scrivi un codice che:
•	salva il tuo nome in una variabile
•	salva la tua età
•	stampa una frase tipo: "Ciao, mi chiamo Anna e ho 21 anni"
'''
nome = "Nicolò"
eta = 19
print(f"Ciao, mi chiamo {nome} e ho {eta} anni")

# Scrivi una funzione somma_pari(lista) che, data una lista di numeri interi, restituisce la somma di tutti i numeri pari presenti nella lista.
def somma_pari(lista):
    somma = 0
    for numero in lista:
        if numero % 2 == 0:
            somma += numero
    return somma

# Scrivi una funzione max_assoluto(lista) che prende una lista di numeri (positivi e negativi) e restituisce il valore con il massimo valore assoluto.
def max_assoluto(lista):
    max_assoluto = 0
    for numero in lista:
        valore_assoluto = abs(numero)
        if valore_assoluto > max_assoluto:
            max_assoluto = valore_assoluto
    return max_assoluto

'''
Scrivi una funzione ricorsiva trova_elemento(lista, x) che dato un array lista e un valore x restituisce True 
se x è presente nella lista, False altrimenti.
'''
def trova_elemento(lista, x):
    if lista == []:
        return False
    elif lista[0] == x:
        return True
    else:
        return trova_elemento(lista[1:], x)
    
# Scrivi una funzione ricorsiva che calcoli la somma degli elementi di una lista di numeri interi.
def somma_lista(lista):
    if lista == []:
        return 0
    else: 
        somma = lista[0]
        return somma + somma_lista(lista[1:])
    
# Scrivi una funzione ricorsiva conta_pari(lista) che conta quanti numeri pari ci sono nella lista.
def conta_pari(lista):
    if not lista:
        return 0
    return (1 if lista[0] % 2 == 0 else 0) + conta_pari(lista[1:])

        