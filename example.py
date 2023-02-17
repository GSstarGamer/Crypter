from main import *

#To make letter data (only run if u want new 100 char letter data)
maker.main(100)

#Paste in code once run example 

with open('data/100.txt', 'r') as f:exec(f.read()) #letter data saved as letters


# to encrypt

crypter.encrypt('I love cats', letters) 

# to decrypt
x = crypter.encrypt('Encrypted text', letters) 
crypter.decrypt(x, letters)

#ofc u need to print them to see its a return :skull: