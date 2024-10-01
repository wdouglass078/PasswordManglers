import random
import sys
#using an api created by Martin Majlis
import wikipediaapi

#this takes in a file of words related to the original password
#and pumps out a new password
def main():
    n = len(sys.argv)
    if n != 3:
        print('error')
        return
    elif sys.argv[1] == '-get':
        #output a file
        makeList(sys.argv[2])
    elif sys.argv[1] == '-generate':
        generatePassword(parse())
    return
    
def parse(): 
    #reading all lines into a list
    fName = 'wordbank.txt'

    with open(fName, 'r') as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        return
    
    #strip all newlines
    i = 0
    while i < len(lines):
        lines[i] = lines[i].strip()
        i+=1
    return lines

def generatePassword(lines):
    random.seed()
    num = random.randrange(0,len(lines))
    password = lines[num]

    i = 0
    while i != 3:
        num = random.randrange(0,10)
        password += str(num)
        i+=1
    password = capitalization(password)
    print(password)
    
def capitalization(p):
    random.seed()
    index = 0
    for x in p:
        if bool(random.getrandbits(1)):
            #capitalize
            p = p[:index] + p[index].upper() + p[index + 1:]
        index += 1
    return p

def makeList(password):
    #make a call to wikipedia article with password get 
    #all the text, strip it, then pipe it through chatgpt
    #still need a way to get to chatgpt or some other ai, 
    #don't knowhow.
    
    #user-agent string, contains project name and contact info.
    wiki = wikipediaapi.Wikipedia('CustomWordBanks (douglasswilliam56@gmail.com)', 'en')

    #what will most likely need to be done is capitalize the first letter, then grab the page
    #sometimes it will automatically capitalize the first letter, but no such guarantee is made.
    if password == '':
        print('password is empty')
        return
    
    page = wiki.page(password)
    if page.exists():
        #pipe every word into a list, which is then turned into a set, removing non-unique entries
        myList = page.text.split()
        mySet = set()
        for x in myList:
            mySet.add(x)

        #output all the words
        myFile = open('wordbank.txt','w')
        for x in mySet:
            try:
                #these conditions filter out short words and strings with numbers or symbols.
                if (len(x) > 2) and x.isalpha():
                    myFile.write(x + '\n')
            except UnicodeEncodeError: 
                print("Bad character or string, skipping...")
        myFile.close
    else:
        print('No "' + password + '"page exists')
    return

    

if __name__ == "__main__":  
    main()