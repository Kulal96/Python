import random
from hangman_arts import logo
from hangman_arts import stages
from hangman_words import word_list

#word_list = ["aardvark", "baboon", "camel"]
print(logo)

lives=6
display=[]
chosen_word=random.choice(word_list)
print(chosen_word)


#generating the blanks as same as chosenword
for i in range(len(chosen_word)):
    display.append("_")

end_of_games=False
while end_of_games==False:
    guess=input("Guess a letter: ").lower()
    #comparing the user alphabet with chosen word
    if guess in display:
        print("Already guessed")
    else:

        for i in range(len(chosen_word)):
            if guess==chosen_word[i]:
                display[i]=chosen_word[i]
            
        #if guessed word is not in chosen_word
        if guess not in chosen_word:
            print(f"guessed letter is {guess},thats not in word.You loose life!")
            lives-=1
            print(stages[lives])
                

        print(f"{' '.join(display)}")

        
        if "_" not in display:
            end_of_games=True
            print("You win")
        elif lives==0:
            end_of_games=True
            print("You lose")
