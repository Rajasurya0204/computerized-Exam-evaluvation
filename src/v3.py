import wikipedia as wiki
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.corpus import wordnet
from crop import getKey


status=""

#loads the dictionary
def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

ps = PorterStemmer()

def main(q,i,k,m):
	global status
	english_words = load_words()
	image = ""
	u_input = ""
	if not i:
		image = '../data/line.jpg'
	else:
		image = '../data/'+i+'.jpg'
	if not q:
		u_input = input("Enter the word to search:")
	else:
		u_input = q
	suggestions = wiki.search(u_input)
	try:
		# getting keys from wiki and removing stop words
		page = wiki.page(u_input)
		key_para = page.summary
		stop_words = set(stopwords.words('english')) 
		word_tokens = word_tokenize(key_para) 
		filtered_words = [w for w in word_tokens if not w in stop_words] 
		filtered_words = [word.lower() for word in filtered_words]
		filtered_words = set(filtered_words)
		status = "[*]CONVERTING YOUR ANSWER IMAGE TO TEXT"
		print("#"*30+"\n"+status)

		# getting keys from answer and removing stop words and making sure it is an english word	
		filtered_answer = getKey(image)
		filtered_answer = [word.lower() for word in filtered_answer]
		filtered_answer = set(filtered_answer)
		#stemmed_answer = [ps.stem(w) for w in filtered_answer]
		#stemmed_answer = set(stemmed_answer)
		stemmed_answer = [word for word in filtered_answer if word in english_words]
		status = "[*]THE KEYWORDS FROM THE ANSWER ARE RECOGNISED"
		print("#"*30+"\n"+status)
		print("#"*30+"\n"+status+"\nKEYWORDS:")
		for word in stemmed_answer:
			print(word,end=",")
		print()
		# stemmed_words = [ps.stem(w) for w in filtered_words]
		# stemmed_words = set(stemmed_words)

		#adding synonyms
		stemmed_word = [word for word in filtered_words if word in english_words]
		stemmed_wordsa = []
		stemmed_words = []
		for word in stemmed_word:
			syns = wordnet.synsets(word)
			synonym = [l.name() for s in syns for l in s.lemmas()]
			stemmed_wordsa.extend(synonym)
		for word in stemmed_wordsa:
			if '_' in word:
				word = word.split('_')
				stemmed_words.extend(word)
			else:
				stemmed_words.append(word)
		status = "[*]THE KEYWORDS FROM THE WIKI ARE COLLECTED AND SYNONYMS ARE ADDED"
		print("#"*30+"\n"+status)
		# for word in stemmed_words:
		# 	print(word,end=",")
		# print()
		
		#option to add more kewyords manually
		# option = input("#"*30+"\nDo you want to add more keywords?")
		# manual= ["y","yes"]
		# option = '0'
		# if option.lower() in manual or option == '1':
		if k:
			# add = input("Enter the words separated with space:").split()
			# add = ps.stem(add)
			stemmed_words.extend(k)
		stemmed_words = set(stemmed_words)
		print(stemmed_words)

		#matching and evaluating
		match = []
		for word in stemmed_answer:
			if word in stemmed_words:
				match.append(word)
		match = set(match)
		mark = m * len(match)
		if mark > 2:
			mark = 2

		print("#"*30+"\nYOUR MARK IS "+ str(mark))
		return mark
	except wiki.exceptions.DisambiguationError as e:
		print("Disambiguation Occured. Select One of the following:")
		print(e.options)
	except wiki.exceptions.PageError as e:
		if suggestions == None:
			print("The page your searching is not available and no suggestions")
		else:
			print("The page your searching is not available. Did you mean?")
			for suggestion in suggestions:
				print(suggestion)

if __name__ == '__main__':
	main('travel','line','',0.25)