def find_anagrams(word, candidates):
    # Initialise results list
    anagram_words = []

    # Make lowercase
    lower_word = word.lower()

    # Check all candidate words
    for candidate in candidates:
        # Initialise the check as fine
        check = 1

        # Make lowercase
        lower_candidate = candidate.lower()
        
        # Check length of words are equal
        if len(candidate) != len(word):
            check = 0

        # Check candidate is not the original word
        elif lower_candidate == lower_word:
            check = 0

        else: 
            # Check each letter in the candidate and see if it's in word
            
            for letter in lower_candidate:
                # Number of ppearances must be equal
                if lower_candidate.count(letter) != lower_word.count(letter):
                    check = 0
                    break
            if check == 1:
                anagram_words.append(candidate)
    
    return(anagram_words)
