import random

words = ['python', 'hangman', 'program','guess', 'game', 'code', 'challenge']

def word_select():
    choice_rand = random.choice(words)
    return choice_rand
def tries_hangman(tries):
    stages = [  
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    \\|//
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    \\|//
                   |      |
                   |    // 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    \\|//
                   |      |
                   |    // \\
                   -
                '''
                
    ]
    return stages[tries]


def hangman():
    word = word_select()
    word_lettr = set(word)
    guess_lettr = set()
    tries = 6

    print(tries_hangman(tries))

    while tries>0:
        display_word = "".join( i if i in guess_lettr else '_' for i in word)
        print(display_word)

        if display_word == word:
            print("correct word guess :",word)
            break
        guess = input("guess a letter: ").lower()
        if guess in guess_lettr:
            print("already guessed try another")
            continue
        guess_lettr.add(guess)

        if guess in word_lettr:
            print("correct guess")

        else:
            print("incorrect you loose a life")
            tries -= 1
            print(tries_hangman(tries)) 
    else:
        print("no more tries")

hangman()
