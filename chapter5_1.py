# -*- coding: utf-8 -*-
# question 3

def count_letters(word,find):
	"""
	Example function with types documented in the docstring.

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

	Exemples
	--------
	>>> count_letters(abracadabra,a)
	5
	>>> count_letters(momomotus,u)
	1
	"""

	count=0
	for i in range(len(word)):
		if word.find(find,i)!=0:
			count+=1	 
	return count

#exemple
print(count_letters('abracadabra','a'))


# question 5

import string

def remove_punctuation(phrase):
	"""
	Example function with types documented in the docstring.

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

#exemple

print(remove_punctuation("Chaine de caractères, passée en paramètre, sans la ponctuation !!!"))

# question 7

def reverse(word) :
	"""
	Example function with types documented in the docstring.

	Ce code doit renverser le mot qui lui est donné en paramètre 

	Parameters
	----------
	param1 : str
		Le 1er paramètre est une chaine de caractères (un mot)

	Returns
	-------
	str
		Chaine de caractères qui est le mot de départ renversé
	"""
	new_word=""
	for i in range(len(word)) :
		new_word=new_word+word[-(i+1)]
	return new_word

# question 8

def mirror(word) :
	"""
	Example function with types documented in the docstring.

	Ce code doit afficher le mot qui lui est donné en paramètre en miroir

	Parameters
	----------
	param1 : str
		Le 1er paramètre est une chaine de caractères (un mot)

	Returns
	-------
	str
		Chaine de caractères qui est le mot de départ écrit comme s'il était lu dans un miroir
	"""
	new_word=word+reverse(word)
	return new_word


