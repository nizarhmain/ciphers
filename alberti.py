from collections import deque
import argparse

parser = argparse.ArgumentParser(
    description='Encipher and decipher using the Alberti\'s cipher')

parser.add_argument(
    "-c", help="the content you are trying to encipher/decipher")
parser.add_argument(
    "-i", help="set the index for the inner disk")
parser.add_argument("-e", action="store_true",
                    help="encrypt the content")
parser.add_argument("-d", action="store_true",
                    help="decrypt the content")

args = parser.parse_args()

inner_ring_index = args.i
content = args.c

stationary_disk = deque('ABCDEFGILMNOPQRSTVXZ1234')
movable_disk = deque('gklnprtuz&xysomqihfdbace')

finalResult = list()


def initMovable(index):
    pos = 0
    for char in movable_disk:
        pos += 1
        if(index == char):
            return pos-1


def initStationary(index):
    pos = 0
    for char in stationary_disk:
        pos += 1
        if(index == char):
            return pos-1


def rotateInnerDisk(newIndex):
    movable_disk.rotate(len(movable_disk) - initMovable(newIndex))


def rotateOuterDisk(newIndex):
    stationary_disk.rotate(initStationary(newIndex) - len(stationary_disk))


def loopThroughContent():
    for char in content:
        pos = 0
        for letter in stationary_disk:
            pos += 1
            if(letter == char):

                finalResult.append(movable_disk[pos-1])
                if (char == '1' or char == '2' or char == '3' or char == '4'):
                    newIndex = movable_disk[initStationary(letter)]
                    rotateInnerDisk(newIndex)

def loopThroughContentOpposite():
	for char in content:
		for x in range(len(movable_disk)):
			moveablePiece = movable_disk[x]
			stationaryPiece = stationary_disk[x]
			if(char == moveablePiece):
				if(stationaryPiece == '1' or stationaryPiece == '2' or stationaryPiece == '3' or stationaryPiece == '4'):
					rotateInnerDisk(moveablePiece)
				finalResult.append(stationary_disk[x])

rotateInnerDisk(args.i)


if(args.e):
    loopThroughContent()

if(args.d):
    loopThroughContentOpposite()

finalString = ""
for piece in finalResult:
	finalString += piece

print(finalString)