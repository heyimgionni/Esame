Documentazione Esercizi 

Es 1 

Come moduli importati ho importato json per lavorare con file json e ipaddress per lavorare con gli indirizzi ip 

# Read the JSON file
with open("address.json") as j:
    data = json.load(j)




# Create the network object for the 192.168.0.0/24 subnet
network = ipaddress.IPv4Network("192.168.0.0/24")


Creiamo la lista dei prefissi mac 
mac_prefix_list = {}

if ip_address:
        ip_obj = ipaddress.IPv4Address(ip_address)
        if ip_obj in network:
            clean_mac_address = mac["mac_address"].split(":")[:3]
            mac_prefix = ":".join(clean_mac_address)
            # Check if this prefix has been encountered before
            if mac_prefix in mac_prefix_list:
                print(f"Sono Dello Stesso Produttore: {mac_prefix_list[mac_prefix]} con indirizzo {mac_prefix_list[mac_prefix]} and {mac['mac_address']} con indirizzo {ip_address}")
            else:
                mac_prefix_list[mac_prefix] = mac["mac_address"]
        else:
            print(f"IP {ip_address} is not in the 192.168.0.0/24 network.")


Creiamo l’obj ip_obj e se è presente nel network allora splittiamo il mac_address e ne prendiamo le prime 6 cifre e se il mac_address si trova nella lista poc’anzi creata printiamo.


Es2 

I moduli che importiamo qui sono sempre due e sono socket e sys 

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



Qui creiamo la funzione di scan delle porte su un host.
Mettiamo dentro un blocco try catch e creiamo per prima cosa il socket.
Connettiamo il socket all’host e alla porta , non usiamo .connect bensì connet_ex in quanto più veloce e non genera errori ma ritorna numeri che possiamo usare per capire se la porta è aperta oppure chiusa.

# if we pass less than two arg in the console we have an error
if len(sys.argv) < 2:
    print("Errore: Devi specificare almeno una porta da verificare.")
    sys.exit(1)
   
# getting the ports from console input
porte = sys.argv[1:]


# we take the ip address
print("Inserisci l'indirizzo IP da verificare:")
ip = input()




Prendiamo le nostre porte e l’indirizzo ip

try:
    socket.inet_aton(ip)  # try to convert to a 32 format ip with inet_aton()
except socket.error:
    print(f"Errore: l'indirizzo IP {ip} non è valido.")
    sys.exit(1)

Per capire se l’indirizzo è valido lo proviamo a convertire in un formato con punti con il metodo inet_aton fornito dal modulo socket 

for porta in porte:
    try:
        porta = int(porta)  # convert from str to int
        stato = scan_porta(ip, porta)  # and try if the port is open or close
        print(f"Porta {porta}: {stato}")
    except ValueError:
        print(f"Errore: la porta '{porta}' non è un numero valido.")



E infine controlliamo le porte lanciando la nostra funzione.


Es3 

In questo caso riportiamo solo un modulo 
import sys

def handle_string(s, n):
    new_string = []
    for word in s:
        for i in range(0, n):
            new_string.append(word)
    return "".join(new_string)

In questo caso prendiamo una stringa e un numero di volte in cui ripetiamo i caratteri singoli della stringa.
if len(sys.argv) != 3:
    print("Errore: Devi fornire una stringa e un numero di volte per ripetere.")
    sys.exit(1)


s = sys.argv[1]
n = int(sys.argv[2])  




new_string = handle_string(s, n)
print(new_string)

Controllo nell’input dello user e poi lanciamo la nostra funzione.


Es4 

Importiamo due moduli

import sys
import csv

Una sola funzione 

def handle_file(user, csv_file):
    user_prio = {}
    # read the file
    with open(csv_file, newline='') as fp:
        reader = csv.reader(fp)
        # skip the header
        next(reader)
        for row in reader:
            name, prio = row
            # check if is a digit the priority
            if prio.isdigit():
                user_prio[name] = int(prio)


In questa funzione prendiamo in input user e un file csv 
Lo leggiamo e saltiamo la prima riga ( intestazione ) 
Creiamo le nostre righe e proviamo a convertire prio ( priority ) in un intero
isFound = None
    if user in user_prio:
        isFound = (user, user_prio[user])
        print(f"User {user} found with priority {user_prio[user]}")

Per controllare se lo user inserito da tastiera esiste , e se lo abbiamo trovato passiamo la linea di dizionario a isFound 

else:
        print(f"User {user} not found.")


if isFound:
        user_prio = {isFound[0]: isFound[1] , **dict(sorted(user_prio.items(), key=lambda item: item[1]))} #we place isFound on top and unpack the rest of the dict
        return user_prio


Se il nostro user esiste modifichiamo il nostro dizionario posizionando lo user a monte e unpacketando il dizionario lo sortiamo in maniera crescente.


eturn dict(sorted(user_prio.items(), key=lambda item: item[1]))
 Se non esiste l’unica cosa che facciamo e restituire il dizionario ordinato 


if len(sys.argv) != 3:
    print("Errore: Devi Fornire Il Nome Dello User E Il File...")
    sys.exit(1)


user = sys.argv[1]
file = sys.argv[2]
print(handle_file(user, file))


Controlliamo l’input su console e lanciamo la nostra funzione 

Es 5 – Encoder 

def encoder(s):
    new_string = [] # new string --> the array with the ascii values and total
    sum = 0
    for word in s:
        new_string.append(ord(word) + 32) # we add 32 to the value and it means blank space
        sum+=(ord(word) + 32) # calculate the sum
    new_string.append(sum) # append the sum
    return new_string # we return it



In questo caso tramutiamo ogni carattere nel valore ascii corrispondente e aggiungiamo 32 che è il valore dello spazio nella tabella ascii 
Sommiamo tutti i valori e restituiamo la stringa 

encoded_str = encoder("STEFANO")
encoded_str_txt = " ".join(map(str,encoded_str))
with open("encode.txt" ,"w") as fw:
    fw.write(encoded_str_txt)




Qui creiamo il nostro file con la parola encodata 

Es 5 – Decode 

def decoder(s):
    decoded_string = [] # the new string
    for value in s:  # for the ascii value in the string
        decoded_string.append(chr(value - 32))  # we transform it in the char - 32
    decoded_string.pop(len(decoded_string) - 1) # we pop of the last value that is the sum of ASCCI CHAR --> :
    return ''.join(decoded_string)


with open("encode.txt" , "r") as fp:
    values = list(map(int, fp.read().split()))
    decoded_str = decoder(values)
with open("decode.txt" , "w") as fw:
    fw.write(decoded_str)

Operazione inversa , infine leggiamo il file e poi ne scriviamo uno nuovo con la parola decodata.

Es 6

Importiamo un solo modulo 

import csv

def handle_users(csv_file):
    # dict to store , names and ip address
    users = {}
    with open(csv_file, newline='') as fp:
        reader = csv.reader(fp)
        for row in reader:
            name, ip_address = row #name and ip_address will be our items
            users[ip_address] = name
    return users



Leggiamo il file degli user 

def handle_traffic(txt_file):
    # dict to store our ip address and our count of times we see the ip in the traffic file
    traffic = {}  
    with open(txt_file, "r") as fp:
        for line in fp:
            _, ip = line.split(" - ") # we put our ip address
            ip = ip.strip()
            if ip in traffic: # if the ip address is in traffic we add one else we have one
                traffic[ip] += 1
            else:
                traffic[ip] = 1
            # we will use this condition to work with max
    return traffic

Leggiamo il log del traffico e se l’ip dello user è ripetuto all’interno del nostro dizionario traffic aggiungiamo un count 

def max_traffic_users(traffic, users): # we pass the traffic and the users
    max_traffic = max(traffic.values()) # max of all values
    max_traffic_ips = [ip for ip, count in traffic.items() if count == max_traffic] # we check if the count is equal to the max_traffic with list conprehensive
    max_traffic_users = [users[ip] for ip in max_traffic_ips] # and here we now wich are the users with more traffic
    return max_traffic_users


Con questa funzione troviamo il massimo dei conteggi di traffic, poi restituiamo gli ip con i conteggi uguali al traffico massimo e ne determiniamo lo user e infine restituiamo 

# we upload our files
csv_file = "utenti.csv"
txt_file = "traffico.txt"
users = handle_users(csv_file)
traffic = handle_traffic(txt_file)


result = max_traffic_users(traffic, users)


print("Gli utenti con il massimo traffico di rete sono:")
for user in result:
    print(user)



Upload dei file e lanciamo la nostra funzione 
