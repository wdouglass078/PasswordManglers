import requests
import random

def main():
    #anagramica api, which only allows for up to 9 letters
    #if there are symbols, they are not considered although
    #they still contribute to the length
    endpoint = "http://www.anagramica.com/all/:"

    #if the password is longer than 9, truncate for the endpt
    #but keep
    password = "password"
    endpoint += (password)

    response = requests.get(endpoint)

    #just checks if it website responded without an error
    if(response.status_code == 200):
        #scramble finds an anagram of the word, and places the remaining
        #unused chars at the end in random order
        newPassword = scramble(response,password, True)
        #capitalization randomly capitalizes none/some/all chars
        newPassword = capitalization(newPassword)
        print(newPassword)
    else: 
        print("Error. Please check the input")

def randomNums(p):
    random.seed()
    i = 0
    while i != 3:
        num = random.randrange(0,10)
        p += str(num)
        i+=1
    return p

def capitalization(p):
    random.seed()
    index = 0
    for x in p:
        if bool(random.getrandbits(1)):
            #capitalize
            p = p[:index] + p[index].upper() + p[index + 1:]
        index += 1
    return p

def scramble(response, oldPassword, doNums):
    #below is a list of all possible anagrams
    anagrams = response.json().get('all')
    
    #save the first ten anagrams
    i = 0
    wordbank = []
    for x in anagrams:
        if i == 10:
            break
        else:
            wordbank.append(x)
        i+=1
    
    #randomly use one of the first ten, then append the rest of the letters
    random.seed()
    num = random.randrange(1,len(wordbank))
    newPassword = wordbank[num]
    
    #append the rest of the letters
    #for loops remove the letters found in the new password
    for x in newPassword:
        for y in oldPassword:
            if x == y:
                oldPassword = oldPassword.replace(x, "", 1)
                break
    
    #add 3 randomly generated numbers
    if doNums:
        newPassword = randomNums(newPassword)
    
    #while appends the remaining letters of the old password in random fashion
    while len(oldPassword) > 0:
        temp = ""
        if len(oldPassword) == 1:
            temp = oldPassword[0]
        else:
            temp = oldPassword[random.randrange(1,len(oldPassword))]
        newPassword += temp
        oldPassword = oldPassword.replace(temp, "", 1)
    print(newPassword)
    return newPassword

if __name__ == "__main__":  
    main()
