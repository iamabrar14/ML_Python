numOfDigits=0
numOfWords=0
numOfLetters=0
text=input("Enter your text : ")
for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        numOfLetters=numOfLetters+1
    elif x>='0' and x<='9':
        numOfDigits=numOfDigits+1
    elif x==' ':
        numOfWords=numOfWords+1

print("Number of words here : ",numOfWords+1)
print("Number of digits here :",numOfDigits)
print("Number of letters here : ",numOfLetters)
