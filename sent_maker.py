
sentence = ""

while True:

    # Get user input of new word or punctuation
    word = input("Enter a word in the sentence (enter . ! ? to end) ")
    sentence = sentence+" "+word
    print(sentence)
    
    if word == '.':
        break
    elif word == '!':
        break
    elif word == '?':
        break
    else:
        continue