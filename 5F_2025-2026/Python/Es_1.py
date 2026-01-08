# Calcolatrice semplice in Python

def calcolatrice():
    print("Benvenuto nella calcolatrice!")
    print("Operazioni disponibili: +, -, *, /")
    
    while True:
        # Chiedi all'utente l'operazione
        operazione = input("Inserisci l'operazione (+, -, *, /) o 'exit' per uscire: ").strip()
        
        # Controlla se l'utente vuole uscire
        if operazione.lower() == "exit":
            print("Uscita dalla calcolatrice.")
            break
        
        # Controlla se l'operazione è valida
        if operazione not in ["+", "-", "*", "/"]:
            print("Operazione non valida. Riprova.")
            continue
        
        # Chiedi i numeri all'utente
        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except ValueError:
            print("Errore: inserisci solo numeri validi.")
            continue

        # Esegui l'operazione scelta
        if operazione == "+":
            risultato = num1 + num2
        elif operazione == "-":
            risultato = num1 - num2
        elif operazione == "*":
            risultato = num1 * num2
        elif operazione == "/":
            if num2 == 0:
                print("Errore: divisione per zero.")
                continue
            risultato = num1 / num2

        # Mostra il risultato
        print(f"Risultato: {risultato}")

# Avvia la calcolatrice
if __name__ == "__main__":
    calcolatrice()