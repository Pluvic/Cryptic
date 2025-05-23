

def caesarBruteForce(cipherText):
    """
    This function takes a cipher text and attempts to decrypt it using a brute force approach.
    It tries all possible shifts (1-25) and returns the decrypted text for each shift.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []

    for letter in alphabet:
        decryptedText = ""
        for char in cipherText:
            newIndex = (alphabet.index(char) - alphabet.index(letter)) % 26
            decryptedText += alphabet[newIndex]
        results.append(decryptedText)
    return results
