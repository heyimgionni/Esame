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

def max_traffic_users(traffic, users): # we pass the traffic and the users
    max_traffic = max(traffic.values()) # max of all values 
    max_traffic_ips = [ip for ip, count in traffic.items() if count == max_traffic] # we check if the count is equal to the max_traffic with list conprehensive
    max_traffic_users = [users[ip] for ip in max_traffic_ips] # and here we now wich are the users with more traffic
    return max_traffic_users

# we upload our files
csv_file = "utenti.csv"
txt_file = "traffico.txt"
users = handle_users(csv_file)
traffic = handle_traffic(txt_file)

result = max_traffic_users(traffic, users)

print("Gli utenti con il massimo traffico di rete sono:")
for user in result:
    print(user)
