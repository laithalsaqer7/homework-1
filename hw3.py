# Count the number of vowels in a given string.

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels in the sentence: {vowel_count}")