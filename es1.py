import json
import ipaddress

# Read the JSON file
with open("address.json") as j:
    data = json.load(j)

# Create the network object for the 192.168.0.0/24 subnet
network = ipaddress.IPv4Network("192.168.0.0/24")

mac_prefix_list = {}

for mac in data:
    ip_address = mac.get("ip_address") #.get() get the value with the key ip_address
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
