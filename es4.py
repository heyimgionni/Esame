import sys
import csv

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
    # check if the user exist
    isFound = None
    if user in user_prio:
        isFound = (user, user_prio[user])
        print(f"User {user} found with priority {user_prio[user]}")
    else:
        print(f"User {user} not found.")
    if isFound:
        user_prio = {isFound[0]: isFound[1] , **dict(sorted(user_prio.items(), key=lambda item: item[1]))} #we place isFound on top and unpack the rest of the dict 
        return user_prio
    else:
        return dict(sorted(user_prio.items(), key=lambda item: item[1]))

if len(sys.argv) != 3:
    print("Errore: Devi Fornire Il Nome Dello User E Il File...")
    sys.exit(1)

user = sys.argv[1]
file = sys.argv[2]
print(handle_file(user, file))
