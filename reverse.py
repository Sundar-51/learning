print("Hello World")
sentence = "Hello World"
reversed_sentence = (sentence[::-1])
reversed_words = ' '.join(word[::-1] for word in sentence.split())
first_letter = ' '.join(word[:1] for word in sentence.split())  # only first letter
remove_first_letter = ' '.join(word[1:] for word in sentence.split())  # excluding first letter
last_letter = ' '.join(word[-1:] for word in sentence.split())  # only last letter
remove_last_letter = ' '.join(word[:-1] for word in sentence.split())  # only last letter
print("reversed_sentence:", reversed_sentence)
print("reversed_words:", reversed_words)
print("first_letter:", first_letter)
print("remove_first_letter:", remove_first_letter)
print("last_letter:", last_letter)
print("remove_last_letter:", remove_last_letter)

# always the colon side indicates the char to display
# negative sign indicates the reverse
