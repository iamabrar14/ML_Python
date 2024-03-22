from random import randint
for x in range(1,6):
 randomNumber=int(input("Enter your random number between 1 to 5  : "))
 guessNumber=randint(1,6)
 if randomNumber==guessNumber:
  print("Your have won")
 else:
  print("You have lost")
  print("The number was : ",guessNumber)
