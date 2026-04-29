import socket

def prendi_input():
    nome = input("Nome studente: ")
    voti = input ("Voti studente separati da una virgola:")
    
    lista = voti.split(",")
    
    voti_validi= []
    
    for v in lista:
        voto=float(v)
        voti_validi.append(voto)
    
    return nome,voti_validi

def mostra_risultato(risposta):
    dati = risposta.split(",")
    
    print("\n--RISULTATO--")
    print("Nome studente: ",dati[0])
    print("Media studente: ",dati[1])
    print("Esito: ",dati[2])
    print("Voto massimo: ",dati[3])
    print("Voto minimo: ",dati[4])
    
    
def start_client():
    while True:
        print("\n1.Calcola voti")
        print("2.Exit")
        
        scelta=input("Scelta: ")
        
        if scelta == "1":
            nome,voti=prendi_input()
            
            voti_str=""
            for i in range(len(voti)):
                voti_str=voti_str+str(voti[i])
                
                if i< len(voti)-1:
                    voti_str=voti_str+","
            
            messaggio = nome + ";" + voti_str
    
    
            client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect(("127.0.0.1",12345))
            
            client.send(messaggio.encode())
            
            risposta = client.recv(1024).decode()
            
            client.close()
            
            mostra_risultato(risposta)
        
        elif scelta=="2":
            print("USCITA")
            break

if __name__ == "__main__":
    start_client()
    
    
        
