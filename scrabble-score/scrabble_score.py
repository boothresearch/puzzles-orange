def score(word):

    # make word lower case so that caps don't break the program
    word = word.lower()
    # initialize word score, word length, and the number of letters to check
    wordScore = 0
    wordLength = len(word)
    letters = range(0, wordLength)

    # assign point value to each letter in word
    for i in letters:
        if word[i] in ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']:
            letterScore = 1 
        elif word[i] in ['d','g']:
            letterScore = 2
        elif word[i] in ['b','c','m','p']:
            letterScore = 3
        elif word[i] in ['f','h','v','w','y']:
            letterScore = 4
        elif word[i] in ['k']:
            letterScore = 5
        elif word[i] in ['j','x']:
            letterScore = 8
        elif word[i] in ['q','z']:
            letterScore = 10
        elif word[i] in ['']: 
            letterScore = 0

        # Add most recent letter score to word score
        wordScore = wordScore + letterScore

    # Print the score of the word
    return wordScore

