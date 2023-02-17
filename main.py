import PyUtls as logger
logger.settings.printCap = False


class maker:
    letters = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '',
               'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': ''}

    def write(filetodo, text):
        with open(f'data/{filetodo}', 'a') as f:
            f.write(text)

    def randomString(lenChars):
        from random import choice
        letters = '''qwertyuiopasdfghjklzxcvbnm1234567890`-=[];,./{}|:<>?!@#$%^&*()'''
        todo = ''
        for i in range(lenChars+1):
            todo += choice(letters)
        return todo

    def main(lenChars):
        import os
        if 'data' not in os.listdir('.'):
            os.mkdir('data')
        filetodo = f'{lenChars}.txt'

        open(f'data/{filetodo}', 'w')

        maker.write(filetodo, 'letters = {\n')
        for letter in maker.letters.keys():
            maker.write(
                filetodo, f"   '{letter}':'{maker.randomString(lenChars)}',\n")

        maker.write(
            filetodo, f"   ' ':'{maker.randomString(lenChars)}',\n")

        maker.write(
            filetodo, f"   'SEP':'{maker.randomString(lenChars)}'\n")

        maker.write(filetodo, '}')
        logger.success(f"Done creating file please use this code to import values with")
        logger.log(f"with open('data/{lenChars}.txt', 'r') as f:exec(f.read())")
        logger.log("value is stored as 'letters'")


class crypter:
    def encrypt(string, data):
        string = string.lower()
        todo = ''
        for letter in string:
            todo += data[letter]
            todo += data['SEP']
        return todo
        
    def decrypt(string, data):
        string = string.split(data['SEP'])
        todo = ''
        for enc in string:
            for key in data.keys():
                if enc == data[key]:
                    todo += key
        return todo