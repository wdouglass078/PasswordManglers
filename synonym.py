# this creates a wordbank using synonyms 
# of the original password
# this uses an api from API Ninjas's free thesaurus
# api. This cannot be used for business purposes until
# another api is found or unless the subscription plan changes

import requests
import sys
import random

def main():
    n = len(sys.argv)
    if n != 2:
        print('error')
        return
    else:
        password = sys.argv[1]
        #check if password is able to be used, working under assumption it does
        endpoint = "https://api.api-ninjas.com/v1/thesaurus?word=" + password
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
    wordbank = response.json().get('synonyms')
    
    newPassword = wordbank[random.randrange(0, len(wordbank))]
    secondWord = wordbank[random.randrange(0,len(wordbank))]
    thirdWord = wordbank[random.randrange(0,len(wordbank))]

    newPassword = newPassword + str(random.randrange(0,10)) + secondWord + str(random.randrange(0,10)) + thirdWord + str(random.randrange(0,10))
    
    return newPassword

def capitalization(p):
    random.seed()
    index = 0
    for x in p:
        if bool(random.getrandbits(1)):
            #capitalize
            p = p[:index] + p[index].upper() + p[index + 1:]
        index += 1
    return p

if __name__ == "__main__":  
    main()