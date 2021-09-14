import re

def abbreviate(name):
    #name=input("Enter name: ")
    name_split= re.split("\s|-", name)

    acronym="" 

    for i in name_split:
        if len(i) == 0:
            continue
        char = i[0]
        if char.isalpha():
            acronym += char.upper()
        else:
            count = 0
            for c in i:
                if c.isalpha():
                    break
                else:
                    count += 1
            if count >= len(i):
                continue
            else:
                char = i[count]
                acronym += char.upper()

    return(acronym)

print(abbreviate("Something - I made up from thin air"))
print(abbreviate("The Road _Not_ Taken"))
print(abbreviate("Complementary metal-oxide semiconductor"))





