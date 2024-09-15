import random
def stage(lives):
    stages=['''
        +--------+
        |        |
        |        O
        |       /|\ 
        |       / \ 
        ============
        ''','''
        +--------+
        |        |
        |        O
        |       /|\ 
        |       / 
        ============
        ''','''
        +--------+
        |        |
        |        O
        |       /|\ 
        |       
        ============
        ''','''
        +--------+
        |        |
        |        O
        |       /|
        | 
        ============
        ''','''
        +--------+
        |        |
        |        O
        |        |
        |
        ============
        ''','''
        +--------+
        |        |
        |        O
        |
        |
        ============
        ''','''
        +--------+
        |        |
        |
        |
        |
        ============
        ''']
    return stages[lives]
name=input("Enter your Name : ")
print(f"Hi {name}, Welcome to Hangman game\n")
print("Lets begin the game...\n")
word_list=["puzzle","python","echo","candle","keyboard","map","potato","mercury"]
lives=6
selected_word=random.choice(word_list)
# print(selected_word)
if selected_word=="puzzle":
    print("Clue : I challenge your mind and test your soule.What am I?")
elif selected_word=="python":
    print("Clue : I can't live without computer I solve problem or perform tasks,What am I?")
elif selected_word=="echo":
    print("clue : I speak without a mouth and hear without ears,What am I?")
elif selected_word=="candle":
    print("Clue : I glow with a warm light,What am I?")
elif selected_word=="keyboard":
    print("Clue : I have keys but open no locks.I have space but no room,What am I?")
elif selected_word=="map":
    print("Clue : I have cities,but no houses.I have mountains,but no trees.I have water,but no fish.What am I?")
elif selected_word=="potato":
    print("Clue : I'm not a fruit,yet I grow underground and I come in different shapes and sizes,What am I?")
elif selected_word=="mercury":
    print("Clue : I am the smallest planet in our solar system,What am I?")
display=[]
for i in range(len(selected_word)):
    display+="_"
print(display)
game_over=False
already_guessed=[]
c=0
while not game_over:
    guessed_letter=input("Guess a letter : ")
    # print(already_guessed)
    if guessed_letter in already_guessed:
        print("You already guessed this letter, try again!")
    else:
        for i in range(len(selected_word)):
            letter=selected_word[i]
            if letter==guessed_letter:
                display[i]=guessed_letter
        print(display)
        if guessed_letter not in selected_word:
            lives=lives-1
            print(f"Sorry, Your guess was incorrect! and you have only {lives} lives")
        else:
            print("Your guess was right!")
        if lives==0:
                game_over=True
                print("Sorry, you lose the game, better luck next time")
                print(f"The correct answer was {selected_word}")
        if '_' not in display:
            game_over=True
            print("Congrats, You won the game")
            print(f"You correctly find the answer: {selected_word}")
        print(stage(lives))
    already_guessed.append(guessed_letter)