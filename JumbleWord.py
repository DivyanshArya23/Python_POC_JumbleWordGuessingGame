#----------------------------------------Load Wordlist in Memory
f=open('wordlist.txt','r')
data=f.read()
wordlist=[]
s=""
for i in data:
    if i!="\n":
        s+=i
    if i=="\n":
        if s!="":
            wordlist.append(s)
            s=""
#----------------------------------------Randomly Select a Word
while len(wordlist)!=0:
    import random
    lenlist=len(wordlist)
    curwordno=random.randint(0,lenlist-1)
    curword=wordlist[curwordno]
    wordlist.pop(curwordno)
#----------------------------------------Break the word in alphabets
    alpha=[]
    for i in curword:
        alpha.append(i)
#----------------------------------------Shuffle the alphabets and make jumbled word
    random.shuffle(alpha)
    jword=""
    for i in alpha:
        jword+=i
#----------------------------------------Start the Game
    print ("Guess the Word:\t",jword)
    guess=""
    while guess!=curword:
        guess=input("Answer:")
        if guess!=curword and guess!="" and guess!="quit()":
            print ("Wrong Answer,Try Again")
        if guess==curword:
            print ("Correct Answer")
        if guess=="quit()":
            quit()

