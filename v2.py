#Version: 02
key_words = ["write","ink","ballpoint","gel"]
qMark = int(input())
marks=[0,1,10]
result = 0
uanswer = []
with open("answer.txt") as answer:
    nWords = 0
    for line in answer:
        nWords = nWords + len(line.split())
        lwords = line.split()
        for word in lwords:
            uanswer.append(word)
if len(uanswer) < marks[qMark]:
    print("The answer is too short :(")
else:
    wordMark = qMark/len(key_words)
    for key in key_words:
        if key in uanswer:
            result += wordMark

print("Your mark is :", result)