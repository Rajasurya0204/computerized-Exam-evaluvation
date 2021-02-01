#Version: 01
key_words = ["write","ink","ballpoint","gel"]
answer = input()
qMark = int(input())
marks=[0,1,10]
result = 0
if len(answer.split()) < marks[qMark]:
    print("The answer is too short :(")
else:
    wordMark = qMark/len(key_words)
    for key in key_words:
        if key in answer:
            result += wordMark
print("Your mark is :", result)

# import nltk
# nltk.download('wordnet')