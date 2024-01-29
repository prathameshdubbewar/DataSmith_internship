def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    stuart_words = []
    kevin_words = []
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
            kevin_words.append(string[i:length])
        else:
            stuart_score += length - i
            stuart_words.append(string[i:length])

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
        print("Words of stuart:", stuart_words)
    elif stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
        print("Words of kevin:", kevin_words)
    else:
        print("Draw")
        print("Words of stuart :", stuart_words)
        print("Words of kevin:", kevin_words)

s = input("Enter a string: ").upper()
minion_game(s)
