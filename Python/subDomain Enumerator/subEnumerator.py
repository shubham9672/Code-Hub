#imports
import requests
import pyfiglet
import time

#function for enumeration of sudomains
def scanner(domainName, subDomain):
    logo = pyfiglet.figlet_format("subEnumerator")
    print(logo)
    time.sleep(1)
    print("[INF] Starting the enumerator")
    time.sleep(1.5)
    print(f"[INF] Enumerating Subdomains for '{domain_name}'")
    time.sleep(1)
    print("[INF]It will take about 4-5 min")

    #loop
    for sub in subDomain:
        url = f"https://{sub}.{domainName}"
        try:
            requests.get(url)
            print(f"[+] {url}")

        except requests.ConnectionError:
            pass

#Main function
if __name__ == '__main__':
    print(" ")
    domain_name = input("Enter the Domain : ")

    with open("./subdomain","r") as file:
        #read the file 
        name = file.read()
        sub_name = name.splitlines()
     #calling the function for scanning the subdomain
    scanner(domain_name,sub_name)