'''
Esercitazione generale (ripasso) - Casa, Cosenza dalle 18:00 alle 18:30

🔁 Esercizio 1 - Somma dei pari

Scrivi una funzione somma_pari(lista) che riceve una lista di interi e restituisce la somma dei numeri pari.

🔸 Esempio: somma_pari([1, 2, 3, 4, 5]) → 6

⸻

🔁 Esercizio 2 - Conta vocali

Scrivi una funzione conta_vocali(stringa) che restituisce il numero di vocali presenti nella stringa data.

🔸 Esempio: conta_vocali("ciao mondo") → 5

⸻

🔁 Esercizio 3 - Max e posizione

Scrivi una funzione max_e_posizione(lista) che restituisce una tupla con il valore massimo in lista e la sua posizione (indice).

🔸 Esempio: max_e_posizione([3, 8, 1, 9]) → (9, 3)

⸻

🔁 Esercizio 4 - Palindromo

Scrivi una funzione palindromo(stringa) che restituisce True se la stringa è palindroma (uguale al contrario), False altrimenti.

🔸 Esempio: "anna" → True, "cane" → False

⸻

🔁 Esercizio 5 - Media dei numeri positivi

Scrivi una funzione media_positivi(lista) che calcola la media dei soli numeri positivi. Se non ci sono numeri positivi, restituisci 0.

🔸 Esempio: media_positivi([1, -2, 3, -1]) → 2.0

⸻

🔁 Esercizio 6 - Fattoriale ricorsivo

Scrivi una funzione fattoriale(n) ricorsiva che calcola il fattoriale di n.

🔸 Esempio: fattoriale(5) → 120

⸻

🔁 Esercizio 7 - Sottolista crescente

Scrivi una funzione sottolista_crescente(lista) che restituisce la più lunga sottolista crescente consecutiva.

🔸 Esempio: [1, 2, 3, 1, 2, 3, 4] → [1, 2, 3, 4]
'''

# Esercizio 1
def somma_pari(lista):
    somma = 0
    for numero in lista:
        if((numero % 2) == 0):
            somma += numero
    return somma

# Esercizio 2
def conta_vocali(stringa):
    count = 0
    for lettera in stringa:
        if lettera.lower() in "aeiou":
            count += 1
    return count

# Esercizio 3
def max_e_posizione(lista):
    max_val = lista[0]
    pos = 0
    for i in range(len(lista)):
        if(lista[i] > max_val):
            max_val = lista[i]
            pos = lista[i]
            pos = i
    return (max_val, pos)

# Esercizio 4
def palindromo(stringa):
    return stringa == stringa[::-1]

# Esercizio 5
def media_positivi(lista):
    positivi = 0
    count = 0
    for numero in lista:
        if(numero > 0):
            positivi += numero
            count += 1
    media = positivi / count
    return media

def fattoriale(n):
    if n == 0 or n == 1:
        return 1
    return n * fattoriale(n-1)

# Esercizio 7
def sottolista_crescente(lista):
    if not lista:
        return []
    max_seq = []
    curr_seq = [lista[0]]
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            curr_seq.append(lista[i])
        else:
            if len(curr_seq) > len(max_seq):
                max_seq = curr_seq
            curr_seq = [lista[i]]
    if len(curr_seq) > len(max_seq):
        max_seq = curr_seq
    return max_seq

    

    