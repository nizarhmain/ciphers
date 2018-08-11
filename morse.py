import argparse

parser = argparse.ArgumentParser(
    description='Encipher and decipher using the caesar\'s shift algorithm')

parser.add_argument("-e", action="store_true", help="encipher the content")
parser.add_argument("-d", action="store_true", help="decipher the content")
parser.add_argument("-shift", help="by how much do I shift it, left or right, give an integer")

parser.add_argument("content", help="the content you are trying to encipher/decipher")

args = parser.parse_args()

print('MORSE CODE')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
morseAlphabet = [
    '._', '_...', '_._.', '_..', '.', '.._.', '__.', '....',
    '..', '.___', '_._', '._..', '__', '_.', '___', '.__.', '__._', '._.', '...', '_',
    '.._', '..._', '.__', '_.._', '_.__', '__..'
]

newpos = []
morseCode = ""

def get_position_in_alphabet(letter):
	pos = 0
	for character in alphabet:
		pos += 1
		if(letter == character):
			return(newpos.append(pos-1))

def get_morseChar(i):
    return str(morseAlphabet[i % len(alphabet)] + "   ")

def generateMorse(string):
	for character in string:
		get_position_in_alphabet(character)
	for pos in newpos:
		global morseCode
		morseCode += get_morseChar(pos)


generateMorse(args.content)
print(morseCode)