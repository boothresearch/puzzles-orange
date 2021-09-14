def count_words(sentence):
    import re

    # Initialise count_dict
    count_dict = {}

    # Convert sentence to list of words
    words = re.split('\s+', sentence)
    print(words)

    for word in words:
        # Remove any punctuation
        word = re.findall("([\w|']+)", word)[0]

        # Remove "'" at the start or end of the word
        word = word.strip('\'')

        # Make word lowercase and add to result dictionary
        word = word.lower()
        print(word)
        # Check if word already in keys
        if word in list(count_dict.keys()):
            # Increase the count
            count = count_dict[word] + 1
            count_dict[word] = count
        else:
            # Otherwise start count at 1
            count_dict[word] = 1
        
    return(count_dict)
    

test = "That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled."
count_words(test)

dict = {'test':1, 'yo':2}
list(dict.keys())[1]
