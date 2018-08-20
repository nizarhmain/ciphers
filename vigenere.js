
const keyword = "nizar"
const plaintext = "thisisamessage"

function fullKeyword() {
	let a = keyword.split("")
	let b = plaintext.split("")
	let c = []
	for (let index = 0; index < plaintext.length; index++) {
		if(index < keyword.length) {
			c.push(a[index])
		} else {
			c.push(c[index - keyword.length])
		}
	}
	return c
}


// manipulation of one shift to the left
const normalAlphabet = ('abcdefghijklmnopqrstuvwxyz').split("")

let alphabet = ('abcdefghijklmnopqrstuvwxyz').split("")

// do manipulations 

// non mutating version
Array.prototype.rotate = function(n) {
    return this.slice(n, this.length).concat(this.slice(0, n));
}



function generateAlphabets() {
	let alphabets = []
	for (let index = 0; index < 26; index++) {
		alphabets.push(alphabet.rotate(index))	
	}
	return alphabets
}



function positionInAlphabet(letter){
	let target;
	normalAlphabet.forEach(element => {
		if(element === letter) {
			target = normalAlphabet.indexOf(element)
		}
	});
	return target
}

function getPositionsOfWord(word) {
	let storedValues = []
	word.split("").forEach(element => {
		storedValues.push(positionInAlphabet(element))
	});
	return storedValues
}


function generateKeywordRows() {
	 tempArray = [];
	 key = fullKeyword().join("")
	 getPositionsOfWord(key).forEach(element => {
		tempArray.push(alphabets[element])		 
	 });
	 return tempArray
}

function plainTextMapping() {
	let positions = getPositionsOfWord(plaintext) 
	let rows = generateKeywordRows()
	for (let index = 0; index < plaintext.length; index++) {
		console.log(rows[index][positions[index]])
	}
}


alphabets = generateAlphabets()
//console.log(generateKeywordRows())
plainTextMapping()

