# =============================================================================

# AUTHOR: Salma Alandary & Benson Liu
# PROGRAM: Caesar Cipher Encoder-Decoder

# =============================================================================

alphabet = "abcdefghijklmnopqrstuvwxyz"

# =============================================================================

# PROJECT FUNCTIONS

# FUNCTION #1: CAESAR CIPHER ENCODER. Write a function that acts as an encoder
# for a Caesar Cipher! Your function should be able to encode a string,
# ignoring characters that do not appear in the alphabet. It should covert all
# upper case characters to lower case in the alphabet. It should be able to
# handle and possible types of values for msg and should handle both positive
# and negative values for shift.
def encode(plaintext, shift):
    output = ""
    for i in plaintext:
        adjusted = i.lower()
        if adjusted in alphabet:
            ordinal = alphabet.index(adjusted)
            shifted = (ordinal + int(shift)) % len(alphabet)
            output += alphabet[shifted]
        else:
            output += i
    return output

# FUNCTION #2: CAESAR CIPHER DECODER. Write a function that acts as an decoder
# for a Caesar Cipher! Your function should be able to encode a string,
# ignoring characters that do not appear in the alphabet. It should covert all
# upper case characters to lower case in the alphabet. It should be able to
# handle and possible types of values for msg and should handle both positive
# and negative values for shift.
def decode(ciphertext, shift):
    output = ""
    for i in ciphertext:
        adjusted = i.lower()
        if adjusted in alphabet:
            ordinal = alphabet.index(adjusted)
            shifted = (ordinal - int(shift)) % len(alphabet)
            output += alphabet[shifted]
        else:
            output += i
    return output

# FUNCTION #3: ROT13 ENCODER-DECODER. ROT13 is a shift cipher where you perform
# a shift by 13. Write a function that acts as both an encoder and decoder for
# ROT 13. Why can the same function be used for encoding and decoding?
# HINT: This can be done in one line if you use one of your previous functions.
def rot13_encode_decode(text):
    return encode(text, 13)

# =============================================================================

# CHALLENGE FUNCTIONS

big_alphabet = " !\"#$%&'()*+',-./013456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# CHALLENGE FUNCTION #1: ASCII CAESAR CIPHER ENCODER. Write a function that
# acts as an encoder for a Caesar Cipher of all the printable ASCII characters!
# Your function should be able to encode a string for any printable ASCII
# character. It should be able to handle and possible types of values for msg
# and should handle both positive and negative values for shift.
def big_encode(plaintext, shift):
    output = ""
    for i in plaintext:
        adjusted = i.lower()
        if adjusted in big_alphabet:
            ordinal = big_alphabet.index(adjusted)
            shifted = (ordinal + int(shift)) % len(big_alphabet)
            output += big_alphabet[shifted]
        else:
            output += i
    return output

# CHALLENGE FUNCTION #2: ASCII CAESAR CIPHER DECODER. Write a function that
# acts as an decoder for a Caesar Cipher of all the printable ASCII characters!
# Your function should be able to decode a string for any printable ASCII
# character. It should be able to handle and possible types of values for msg
# and should handle both positive and negative values for shift.
def big_decode(ciphertext, shift):
    output = ""
    for i in ciphertext:
        adjusted = i.lower()
        if adjusted in big_alphabet:
            ordinal = big_alphabet.index(adjusted)
            shifted = (ordinal - int(shift)) % len(big_alphabet)
            output += big_alphabet[shifted]
        else:
            output += i
    return output

# CHALLENGE FUNCTION #3: CAESAR BRUTE FORCE. Write a function that acts as a
# brute force solver for a Caesar Cipher (you can chose whether to use alphabet
# or big_alphabet in your function). Your function should print out all possible
# combinations of shifts in the given alphabet and the user should be able to find
# their plaintext message in the cipher.
def brute_force(ciphertext):
    for i in range(len(alphabet)):
        decoded = decode(ciphertext, i)
        print("Decoded:", decoded)