'''
Siano prodotti due file: encoder.py e decoder.py.
Il seguente esempio descrive il funzionamento di entrambi gli script.
Supponendo che l’input dello script encoder.py sia la stringa STEFANO
rappresentabile nel modo seguente:
S T E F A N O
il risultato di encoder.py dovrà essere il seguente:
115 116 101 102 97 119 111 752
Supponendo che l’input per decoder.py sia:
115 116 101 102 97 119 111 752
il risultato di decoder.py, dopo aver verificato la correttezza dell’input ricevuto,
dovrà essere la seguente:
S T E F A N O
'''

# encoder 
def encoder(s):
    new_string = [] # new string --> the array with the ascii values and total
    sum = 0
    for word in s:
        new_string.append(ord(word) + 32) # we add 32 to the value and it means blank space
        sum+=(ord(word) + 32) # calculate the sum
    new_string.append(sum) # append the sum
    return new_string # we return it 


# print the results
encoded_str = encoder("STEFANO")
encoded_str_txt = " ".join(map(str,encoded_str))
with open("encode.txt" ,"w") as fw:
    fw.write(encoded_str_txt)
