import wikipedia as wiki
import nltk
from rake_nltk import Rake

r = Rake()

u_input = input("Enter the word to search:")
suggestions = wiki.suggest(u_input)
try:
	page = wiki.page(u_input)
	print(page.content)
except wiki.exceptions.PageError as e:
	if suggestions == None:
		print("The page your searching is not available and no suggestions")
	else:
		print("The page your searching is not available. Did you mean?")
		for suggestion in suggestions:
			print(suggestion)

sentence_list = nltk.sent_tokenize(page.content)
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}  
for word in nltk.word_tokenize(page.content):  
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
sentence_scores = {}  
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
import heapq  
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  
print("+++"*30,summary) 
print("+++"*30)
r.extract_keywords_from_text(summary)
print(r.get_ranked_phrases())
print("+++"*30)
print(page.summary)