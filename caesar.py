import argparse

parser = argparse.ArgumentParser(description='Encipher and decipher using the caesar\'s shift algorithm')

parser.add_argument("-e", action="store_true", help="encipher the content")
parser.add_argument("-d", action="store_true", help="decipher the content")
parser.add_argument("-shift", help="by how much do I shift it, left or right, give an integer")

parser.add_argument("content", help="the content you are trying to encipher/decipher")

args = parser.parse_args()

print('CAESAR\'S CIPHER ')

text = args.content

alphabet = 'abcdefghijklmnopqrstuvwxyz'

newpos = []

def access_char(i):
    return alphabet[i % len(alphabet)]

def get_position_in_alphabet(letter):
    pos = 0
    for character in alphabet:
        pos += 1
        if (letter == character):
            # if we want to encipher, we just encipher the next one basically
            if(args.e):
                newpos.append(pos-1 + int(args.shift))

            # if we want to decipher, we just encipher the previous one
            if(args.d):
                newpos.append(pos-1 - int(args.shift))
            #print(letter + '  at position ' + str(pos))

def loop_through(string):
    for character in string:
        get_position_in_alphabet(character)

def ciphered_string():
    cipheredMessage = ""
    for number in newpos:
        #print(access_char(number))
        cipheredMessage += access_char(number)
    
    print('the ciphered message is : ' + cipheredMessage)

loop_through(text)
ciphered_string()
