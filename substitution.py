with open('alphabet.txt', 'r') as file: 
    alphabet = file.read().strip()  

with open('originalMessage.txt', 'r') as file: 
    originalMessage = file.read().strip()   

# 1 - declare var for new message 
# 2 - make loop for each char in originalMessage
# 3 - search about index of char in alphabet
# 4 - get new char that precedes old char with 3 places in alphabet
# 5 - push new char in new message
# 6 - return new message

def substitution(originalMessage): 
    newMessage = ""
    for char in originalMessage.upper(): 
        if char.isalpha():
            index = alphabet.index(char)
            newChar = alphabet[index -3]
            newMessage += newChar
        else:
            newMessage += char    
    return newMessage

newMessage = substitution(originalMessage)   

with open('newMessage.txt', 'w') as file: 
     file.write(newMessage) 
