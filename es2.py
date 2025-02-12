# import of the libraries --> socket and sys
# https://www.programmareinpython.it/video-corso-python-intermedio/06-il-modulo-socket-introduzione/ --> reference 
import socket
import sys

def scan_porta(host, porta): # function that takes an host and a port
    # we put all of this in a try catch block 
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # we create here our socket
        result = sock.connect_ex((host, porta)) # is more efficient connect_ex then connet --> is twice time more efficienct
        # also connect_ex do not throw and error but return an integer that we can use ( like in C )
        sock.close() #and then we close the socket 
        if result == 0:
            return "aperta"
        else:
            return "chiusa"
    except Exception as e:
        return f"Errore: {e}"

# if we pass less than two arg in the console we have an error
if len(sys.argv) < 2:
    print("Errore: Devi specificare almeno una porta da verificare.")
    sys.exit(1)
    
# getting the ports from console input 
porte = sys.argv[1:]

# we take the ip address
print("Inserisci l'indirizzo IP da verificare:")
ip = input()

try:
    socket.inet_aton(ip)  # try to convert to a 32 format ip with inet_aton()
except socket.error:
    print(f"Errore: l'indirizzo IP {ip} non è valido.")
    sys.exit(1)

# check evry port
for porta in porte:
    try:
        porta = int(porta)  # convert from str to int
        stato = scan_porta(ip, porta)  # and try if the port is open or close
        print(f"Porta {porta}: {stato}")
    except ValueError:
        print(f"Errore: la porta '{porta}' non è un numero valido.")
