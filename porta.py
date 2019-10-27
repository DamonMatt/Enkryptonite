
class PORTA:
    base = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m" ]
    alpha = {
        "ab": [ "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ],
        "cd": [ "z", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" ],
        "ef": [ "y", "z", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x" ],
        "gh": [ "x", "y", "z", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w" ],
        "ij": [ "w", "x", "y", "z", "n", "o", "p", "q", "r", "s", "t", "u", "v" ],
        "kl": [ "v", "w", "x", "y", "z", "n", "o", "p", "q", "r", "s", "t", "u" ],
        "mn": [ "u", "v", "w", "x", "y", "z", "n", "o", "p", "q", "r", "s", "t" ],
        "op": [ "t", "u", "v", "w", "x", "y", "z", "n", "o", "p", "q", "r", "s" ],
        "qr": [ "s", "t", "u", "v", "w", "x", "y", "z", "n", "o", "p", "q", "r" ],
        "st": [ "r", "s", "t", "u", "v", "w", "x", "y", "z", "n", "o", "p", "q" ],
        "uv": [ "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "n", "o", "p" ],
        "wx": [ "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "n", "o" ],
        "yz": [ "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "n" ]
    }

    key = None
    key_size = None
    text = None
    cipher = None

    # isValid = False

    def __init__(self, key):
        if self.VerifyKey(key):
            self.key = key
            self.key_size = len(key)

    def VerifyKey(self, key):
        return key.isalpha()

    def Decrypt(self, cipher):
        self.cipher = cipher
        text = ""
        for index, element in enumerate(self.cipher):
            text += self.EncryptElement(index, element) if element.isalpha() else element
        self.text = text
        return text

    def Encrypt(self, text):
        self.text = text.lower()  
        cipher = ""
        for index, element in enumerate(self.text):
            cipher += self.EncryptElement(index, element) if element.isalpha() else element
        self.cipher = cipher
        return cipher

    def EncryptElement(self, index, element):
        index = index % self.key_size
        for key in self.alpha.keys():
            if self.key[index] in key:
                alpha = self.alpha[key]
        if element in self.base:
            return alpha[ self.base.index(element) ]
        else:
            return self.base[ alpha.index(element) ]

