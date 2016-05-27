class RC4(object):
    """
    Python implementation of the RC4 Cipher.

    CF: Applied Cryptography, Chapter 17 by Bruce Scheneier

    CF: https://www.quora.com/Cryptography-What-is-an-intuitive-explanation-of-the-RC4-encryption-algorithm-and-its-weaknesses

    TODO: Encrypting files (BytesIO), not just strings
    """

    def __init__(self, key="cypher-cossack"):
        """
        RC4 Cipher.

        :param key: Key for to encrypt and decrypt.
        :type key: str
        """
        self.key = key

    @classmethod
    def run_ksa(self, key):
        """
        Performs the Key Scheduling Algorithm from a key.

        Implements Shannon principles of 'confusion' -- obscuring the relationship between the ciphertext and the actual key
        """
        s = [*range(256)]
        j = 0
        for i in range(len(s)):
            j = (j + i + ord(key[i % len(key)])) % 256
            # import ipdb; ipdb.set_trace()
            # print(i, j)
            s[i], s[j] = j, i
        return s

    def run_prga(self, key):
        """
        Performs PRGA (Pseudo-randomnumber [Byte] Generator Algorithm)
        """
        s = self.run_ksa(key)
        i, j = 0, 0
        for x in iter(int, 1):
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = j, i
            k = s[(s[i] + s[j]) % 256]
            yield k

    def encrypt(self, plaintext):
        """
        Encrypts a plaintext with respective cipher.

        XOR's the PRGA against each character bit.

        :param plaintext: Plaintext message
        :type plaintext: str

        :returns: ciphertext
        """
        ciphertext = ""
        prga = self.run_prga(key=self.key)
        for i in plaintext:
            c = next(prga) ^ ord(i)  # XOR's the char against the keystream
            c = hex(c).split('0x')[-1]
            ciphertext += c if len(c) > 1 else "0" + c  # Prepend a leading 0 if the byte is represenetd by a single character. This will help with parsing in decryption phase.
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypts ciphertext

        :Returns: plaintext
        """
        plaintext = ""
        prga = self.run_prga(key=self.key)
        ciphertext = [ciphertext[i: i + 2]for i in range(0, len(ciphertext)) if i % 2 != 1]
        for i in ciphertext:
            p = next(prga) ^ int(i, 16)
            plaintext += chr(p)
        return plaintext
