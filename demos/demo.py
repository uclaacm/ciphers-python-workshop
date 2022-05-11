# =============================================================================
alphabet = "abcdefghijklmnopqrstuvwxyz"
# =============================================================================
#DEMO: We want to implement a caesar shift by three on the following message.
# this implementation does not need to be robust.
our_message = "ciphers are cool"
output = ""
for i in our_message:
    adjusted = i.lower()
    if adjusted in alphabet:
        ordinal = alphabet.index(adjusted)
        shifted = ordinal + 3
        output += alphabet[shifted]
    else:
        output += i
print(output)
# =============================================================================