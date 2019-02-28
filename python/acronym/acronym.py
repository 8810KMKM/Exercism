def isAlphabet(x):
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    return x in alphabet

def abbreviate(words):
    words = words.split()
    acrom = ""
    for word in words:
        word = word.upper()
        if isAlphabet(word[0]):
            acrom += word[0]

        for i in range(len(word) - 1):
            if word[i] != '\'' and not isAlphabet(word[i]):
                acrom += word[i + 1]
            
    return acrom
