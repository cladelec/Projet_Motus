
#2
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
	break
	if letter=="Q" or letter == "O"	:	
		print(letter +"u"+ suffix)
	else :
		print(letter+suffix)

#3

def count_letters(word,find):
"""Example function with types documented in the docstring.

		Ce code doit retourner le nombre d'occurences d'un caractère passé en paramètre dans un mot donné également 

    Parameters
    ----------
    param1 : str
        Le 1er paramètre est une chaine de caractères
    param2 : char
        Le 2ème paramètre est un caractère

    Returns
    -------
    int
        Nombre d'occurences du caractère
    """

	count=0
	for i in range(len(word)):
		if word.find(find,i)!=0:
			count+=1	 
	return count

#5
import string

def remove_punctuation(phrase):
"""Example function with types documented in the docstring.

		Ce code doit renvoyer une chaine de caractère issue d'un extrait dont la ponctuation a été supprimée 

    Parameters
    ----------
    param1 : str
        Le 1er paramètre est une chaine de caractères

    Returns
    -------
    str
        Chaine de caractères passée en paramètre sans la ponctuation
    """
	phrase_sans_punct = ""
	for letter in phrase:
		if letter not in string.punctuation:
			phrase_sans_punct += letter
	return phrase_sans_punct

def question5(text) :
	text2=remove_punctuation(text)
	words=text2.split()
	count=0

	for word in words :
		if "e" in word :
			count+=1
	
	retour='Your text contains '+str(len(words))+' words, of which '+str(count)+' contain an "e".'
	return retour

#6
layout = "{0:>3}{1:>3}{2:>3}{3:>3}{4:>3}{5:>4}{6:>4}{7:>4}{8:>4}{8:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"

#print(layout.format("","1", "2", "3", "4", "5","6","7","8","9","10","11","12"))
for i in range(1, 12):
	break
	print(layout.format(i, i*1,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))

#7
def reverse(word) :
	new_word=""
	for i in range(len(word)) :
		new_word=new_word+word[-(i+1)]
	return new_word

#8
def mirror(word) :
	new_word=word+reverse(word)
	return new_word

#9
def supprime(word,occurence) :
	new_word=""
	for letter in word :
		if letter!=occurence :
			new_word=new_word+letter
	return new_word

#10





