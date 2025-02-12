import sys

def handle_string(s, n): 
    new_string = []
    for word in s: 
        for i in range(0, n): 
            new_string.append(word)
    return "".join(new_string)

if len(sys.argv) != 3:
    print("Errore: Devi fornire una stringa e un numero di volte per ripetere.")
    sys.exit(1)

s = sys.argv[1]
n = int(sys.argv[2])  


new_string = handle_string(s, n)
print(new_string)
