# A global constant for the alphabet is created.
ALPHABET = "abcdefghijklmnñopqrstuvwxyz"

def clean_string(words:str):
    """The objective of the function is to receive a string as input and return a set of all the characters in the alphabet that are present in the input string.

    Args:
        words(str): A string to be evaluated.

    Returns:
        set: A set of strings containing all the characters in the alphabet that are present in the input string.
    """    
    words_clean =set()
    for char in words.lower():
        if char in ALPHABET:
            words_clean.add(char)
    return words_clean

def validate_alphabet(words:str):
    """The objective of the function is to receive a string as input and validate if it contains all the characters in the alphabet.

    Args:
        words (str):  A string to be evaluated.

    Returns:
        bool: The function returns a boolean value (True or False) indicating whether the input string contains all the characters in the alphabet.
    """
    if not isinstance(words, str):
        raise TypeError("Input must be a string")
    word_to_validate = clean_string(words)
    for char in ALPHABET:
        if char not in word_to_validate:
            return False
    return True

print(validate_alphabet.__doc__)
print(clean_string.__doc__)
