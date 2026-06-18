print("Welcome to the Caesar Cipher Encoder!\n")

num_to_shift = int(input("Enter the number of positions to shift (1-25): "))

while num_to_shift < 1 or num_to_shift > 25:
    num_to_shift = int(input("Enter the number of positions to shift: "))

word = input("Enter the word to encode: ")

encoded_word = ""
decoded_word = ""

for letter in word:
    if letter.isupper():
        letter_num = (ord(letter)-65) % 26 + 65
        letter_num += num_to_shift
        encoded_letter = chr(letter_num)
        encoded_word += encoded_letter
    else:
        letter_num = (ord(letter)-97) % 26 + 97
        letter_num += num_to_shift
        encoded_letter = chr(letter_num)
        encoded_word += encoded_letter

print("\nEncoded word: " + encoded_word)

for letter in encoded_word:
    if letter.isupper():
        encoded_letter_num = (ord(letter)-65) % 26 + 65
        encoded_letter_num -= num_to_shift
        decoded_letter = chr(encoded_letter_num)
        decoded_word += decoded_letter
    else:
        encoded_letter_num = (ord(letter)-97) % 26 + 97
        encoded_letter_num -= num_to_shift
        decoded_letter = chr(encoded_letter_num)
        decoded_word += decoded_letter
print("\nDecoded word: " + decoded_word)

print("\nThank you for using the Caesar Cipher Encoder!")