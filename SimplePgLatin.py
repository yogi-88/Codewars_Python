# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# Problem Breakdown
# Split the sentence into words.
# For each word:
# Check if it’s a word or punctuation.
# If it’s a word, move the first letter to the end and add "ay" to the word.
# If it’s punctuation, leave it as is.
# Join all the words (and punctuation) back together into a single sentence.
# Pseudocode
# Here’s a step-by-step pseudocode for solving this:

# Define a function convert_to_pig_latin(sentence).
# Split the sentence into words and punctuation marks (we can use split() which handles this well if there are spaces around punctuation).
# Initialize an empty list pig_latin_words to store transformed words.
# Loop through each word in the list:
# Check if the word is alphabetic (i.e., no punctuation marks).
# If it’s alphabetic, apply Pig Latin rules:
# Move the first letter to the end of the word.
# Append "ay" to the end.
# Add the transformed word to pig_latin_words.
# If it’s not alphabetic (likely punctuation), add it as-is to pig_latin_words.
# Join pig_latin_words into a single string with spaces between them.
# Return the final sentence.

def convert_to_pig_latin(sentence):
    # Split the sentence by spaces to handle each word and punctuation separately
    words = sentence.split()
    pig_latin_words = []

    # Process each word individually
    for word in words:
        # Check if the word is alphabetic (has no punctuation)
        if word.isalpha():
            # Move the first letter to the end and add 'ay'
            pig_latin_word = word[1:] + word[0] + "ay"
            pig_latin_words.append(pig_latin_word)
        else:
            # If it's punctuation or has punctuation, add it unchanged
            pig_latin_words.append(word)

    # Join the modified words back into a sentence
    return " ".join(pig_latin_words)

# Test example
print(convert_to_pig_latin("Hello world!"))

# Other way(my initial try): 
def pig_it(text):

    words = text.split(" ")


    new_list = []
    for word in words:

        if word.isalpha():
            first_letter = word[:1]
            #print(first_letter)
            rest_letters = word[1:]
            #print(rest_letters)
            new_word = rest_letters + first_letter + 'ay'
            #print(new_word)
        else:
            new_word = word
        new_list.append(new_word)
        my_string = ' '.join(new_list)
    return my_string

print(pig_it('Pig latin is cool!'))

# ALternative way(short way):

def pig_it(text):
    lst = text.split()
    return " ".join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in lst])


print(pig_it('Pig latin is cool!'))
