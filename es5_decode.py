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