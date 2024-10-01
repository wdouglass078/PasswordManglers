# this takes the original password, finds a wikipedia 
# article that is close to it, extracts all unique and
# non-common words and uses that as a word bank to generate 
# a new password
import random
import sys
#using an api created by Martin Majlis

import wikipediaapi

def main():
    n = len(sys.argv)
    if n != 2:
        print('error')
        return
    word = sys.argv[1]
    word = generatePassword(word)
    print(word)
    
    return

def generatePassword(password):
    #reading all lines into a list of 500 common words
    fName = '500commonwords.txt'

    with open(fName, 'r') as file:
        lines = file.readlines()
    
    if len(lines) == 0:
        return
    
    #strip all newlines
    i = 0
    while i < len(lines):
        lines[i] = lines[i].strip()
        i+=1

    #access wikipedia page     
    #user-agent string, contains project name and contact info.
    wiki = wikipediaapi.Wikipedia('CustomWordBanks (douglasswilliam56@gmail.com)', 'en')

    #what will most likely need to be done is capitalize the first letter, then grab the page
    #sometimes it will automatically capitalize the first letter, but no such guarantee is made.
    if password == '':
        print('password is empty')
        return ''
    
    page = wiki.page(password)
    if page.exists():
        #pipe every word into a list, which is then turned into a set, removing non-unique entries
        myList = page.text.split()
        mySet = set()
        for x in myList:
            mySet.add(x)
        myList = list(mySet)

        #output all the words, mostly used for testing 
        myFile = open('wordbank.txt','w')
        tmp = list()
        for x in myList:
            #try statement catches 'weird' characters not found in ascii
            try:
                #these conditions filter out short words and strings with numbers or symbols.
                #also filtered out through mySet
                if (len(x) > 2) and x.isalpha() and x not in lines:
                    myFile.write(x + '\n')
                    tmp.append(x)
            except UnicodeEncodeError: 
                print("Bad character or string, skipping...")
        myFile.close
        myList = tmp
    else:
        print('No "' + password + '"page exists')
        return ''

    random.seed()
    num = random.randrange(0,len(myList))

    newPassword = myList[num]
    # from here, we can do whatever to the password
    # we could add more words (highly recommended)
    # and do other things to it (capitalizing, adding 
    # random numbers, etc)
    return newPassword

if __name__ == "__main__":  
    main()