# =============================================================================

# AUTHOR: [your name here]
# PROGRAM: Caesar Cipher Encoder-Decoder

# =============================================================================

alphabet = "abcdefghijklmnopqrstuvwxyz"

# =============================================================================

# DEMO FUNCTIONS! Follow along in the demo!

# DEMO FUNCTION A. MINI-ENCODER. Implement a Caesar Cipher encoder with a shift
# of three.
def mini_encode(plaintext):
    # insert your implementation here
    return "ACM Cyber is cool!"

# DEMO FUNCTION B: MINI-DECODER. Implement a Caesar Cipher decoder with a shift
# of three.
def mini_decode(ciphertext):
    # insert your implementation here
    return "ACM Cyber is cool!"

# =============================================================================

# PROJECT FUNCTIONS

# FUNCTION #1: CAESAR CIPHER ENCODER. Write a function that acts as an encoder
# for a Caesar Cipher! Your function should be able to encode a string,
# ignoring characters that do not appear in the alphabet. It should covert all
# upper case characters to lower case in the alphabet. It should be able to
# handle and possible types of values for msg and should handle both positive
# and negative values for shift.
def encode(plaintext, shift):
    # insert your implementation here
    return "ACM Cyber is cool!"

# FUNCTION #2: CAESAR CIPHER DECODER. Write a function that acts as an decoder
# for a Caesar Cipher! Your function should be able to encode a string,
# ignoring characters that do not appear in the alphabet. It should covert all
# upper case characters to lower case in the alphabet. It should be able to
# handle and possible types of values for msg and should handle both positive
# and negative values for shift.
def decode(ciphertext, shifts):
    # insert your implementation here
    return "ACM Cyber is cool!"

# FUNCTION #3: ROT13 ENCODER-DECODER. ROT13 is a shift cipher where you perform
# a shift by 13. Write a function that acts as both an encoder and decoder for
# ROT 13. Why can the same function be used for encoding and decoding?
# HINT: This can be done in one line if you use one of your previous functions.
def rot13_encode_decode(text):
    # insert your implementation here
    return "ACM Cyber is cool!"

# =============================================================================

# CHALLENGE FUNCTIONS

big_alphabet = " !\"#$%&'()*+',-./013456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# CHALLENGE FUNCTION #1: ASCII CAESAR CIPHER ENCODER. Write a function that
# acts as an encoder for a Caesar Cipher of all the printable ASCII characters!
# Your function should be able to encode a string for any printable ASCII
# character. It should be able to handle and possible types of values for msg
# and should handle both positive and negative values for shift.
def big_encode(plaintext, shift):
    # insert your implementation here
    return "ACM Cyber is cool!"

# CHALLENGE FUNCTION #2: ASCII CAESAR CIPHER DECODER. Write a function that
# acts as an decoder for a Caesar Cipher of all the printable ASCII characters!
# Your function should be able to decode a string for any printable ASCII
# character. It should be able to handle and possible types of values for msg
# and should handle both positive and negative values for shift.
def big_decode(ciphertext, shift):
    # insert your implementation here
    return "ACM Cyber is cool!"

# CHALLENGE FUNCTION #3: CAESAR BRUTE FORCE. Write a function that acts as a
# brute force solver for a Caesar Cipher (you can chose whether to use alphabet
# or big_alphabet in your function). Your function should print out all possible
# combinations of shifts in the given alphabet and the user should be able to find
# their plaintext message in the cipher.
def brute_force(ciphertext):
    # insert your implementation here
    return "ACM Cyber is cool!"