def word_count(sentence):
    words = sentence.split()
    word_dict = {}

    for word in words:

        cleaned_word = word.strip(".,!?").lower()

        if cleaned_word:
            if cleaned_word in word_dict:
                word_dict[cleaned_word] += 1
            else:
                word_dict[cleaned_word] = 1

    return word_dict

input_sentence = input("Enter a sentence: ")


word_occurrences = word_count(input_sentence)
print("Word occurrences:", word_occurrences)
