from string import ascii_letters


def encrypt(string, shift):
    """
    Time complexity: O(n)
    """
    alphabet = ascii_letters
    result = ""

    for char in string:
        if char not in alphabet:
            result += char
        else:
            new_key = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_key]
    return result


def decrypt(string, shift):
    shift *= -1
    return encrypt(string, shift)
