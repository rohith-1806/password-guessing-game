import random
easy_words = ["apple","train","truck","tiger","money","india","goa","pen","bat"]
medium_words = ["python","battle","mobile","laptop bag","brush",'pillow']
hard_words = ["bear","elephant","ostrich","girafiee","psycho","mountain","strawberry"]

print("welcome to the password guesssing game")
print("choose a diffuculty level for the game: easy,medium or hard") 

level = input("enter your diffuculty level : ").lower().strip()

if level == "easy":
     secret = random.choice(easy_words)


elif level == "medium":
     secret = random.choice(medium_words)


elif level == "hard":
     secret = random.choice(hard_words)


else:
     print("invaid level selection,hence throwing into easy level")
     secret = random.choice(easy_words)


attempts = 0

print("\n guess the secret password")

while True:

    

    guess = input("enter your guess or exit:").lower()
    attempts +=1

    if guess == "exit":
     print("thanks for visiting have a nice day" )
     break

    if guess == secret:
        print(f"congratulations your guessed the word in {attempts}  attempt")
        break
    hint = " "
    
    for i in range (len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("hint :" , hint)

print("game over,\nthanks for playing hope you enjoyed")
