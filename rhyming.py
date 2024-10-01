# this idea involves finding words that
# rhyme with the original password
# a rhyming api was found thru API Ninjas.

import requests
import random
import sys

def main():
    n = len(sys.argv)
    if n != 2:
        print('error')
        return
    else:
        password = sys.argv[1]
        #check if password is able to be used, working under assumption it does
        endpoint = "https://api.api-ninjas.com/v1/rhyme?word=" + password
        response = requests.get(endpoint, headers={'X-Api-Key': 'DyFwQxrA2BHRhCtrwGssmA==rCaB1gzdZbkIGEv7'})
        
        if response.status_code == 200:
            newPassword = (generatePassword(response))
            newPassword = capitalization(newPassword)
            print(newPassword)
        else: 
            print('server error')
    return

def generatePassword(response):
    random.seed()
    #list of all synonyms
    wordbank = response.json().get()
    newPassword = ''
    return newPassword

if __name__ == "__main__":  
    main()