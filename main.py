import parse_txt
import geo_lookup
import RDAP
import requests_cache

requests_cache.install_cache('cache')
dictionary = parse_txt.parseText("list_of_ips.txt")

print("Welcome, enter 'keys' to see the list of keys and 'quit' at any time to exit out.")
userInput = "true"

while userInput != "quit":

    userInput = input("Choose an IP via its corresponding key : ")

    if userInput == "quit":
        break
    elif userInput == "keys":
        print(dictionary)
    elif not userInput.isdigit():
        print("Please enter an appropriate input")
        continue

    else:
        print(f'You have chosen {dictionary[int(userInput)]} as your ip')
        ip = dictionary[int(userInput)]

        print("Would you like to perform a Geo IP or a RDAP lookup?")
        userInput = input("Enter 1 for Geo, 2 for RDAP, 3 to return : ")

        if userInput == "quit":
            break
        elif userInput == '1':
            geo_lookup.geoLookup(ip)

        elif userInput == '2':
            print("Would you like to perform a basic RDAP lookup or a detailed lookup?")
            userInput = input("Enter 1 for basic, 2 for detailed : ")
            if userInput == "quit":
                break
            elif userInput == '1':
                RDAP.rdapLookup_b(ip)
            elif userInput == '2':
                RDAP.rdapLookup_d(ip)
            else:
                print("Please enter an appropriate input")

        elif userInput == '3':
            print("Returning")
        else:
            print("Please enter an appropriate input")
