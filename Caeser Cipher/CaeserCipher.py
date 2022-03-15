"""Caesar Cipher
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters."""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing.


class CaeserCipher:
    # Every possible symbol that can be encrypted/decrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @property
    def mode(self):
        # Let the user enter if they are encrypting or decrypting:
        while True:  # Keep asking until the user enters e or d.
            print('Do you want to (e)ncrypt or (d)ecrypt?')
            response = input('> ').lower()
            if response.startswith('e'):
                return 'encrypt'
            elif response.startswith('d'):
                return 'decrypt'

            print('Please enter the letter e or d.')

    @property
    def key(self):
        # Let the user enter the key to use:
        while True:  # Keep asking until the user enters a valid key.
            maxKey = len(self.SYMBOLS) - 1
            print('Please enter the key (0 to {}) to use.'.format(maxKey))
            response = input('> ').upper()
            if not response.isdecimal():
                continue

            if 0 <= int(response) < len(self. SYMBOLS):
                return int(response)

    @property
    def message(self):
        # Caesar cipher only works on uppercase letters:
        return input('> ').upper()

    def translate(self, mode: str, key: int, message: str):
        """Encrypt/decrypt each symbol in the message:"""

        # Stores the encrypted/decrypted form of the message:
        translated = ''

        for symbol in message:
            if symbol in self.SYMBOLS:
                # Get the encrypted (or decrypted) number for this symbol.
                # Get the number of the symbol.
                num = self.SYMBOLS.find(symbol)
                if mode == 'encrypt':
                    num += key
                elif mode == 'decrypt':
                    num -= key

                # Handle the wrap-around if num is larger than the length of
                # SYMBOLS or less than 0:
                if num >= len(self.SYMBOLS):
                    num = num - len(self.SYMBOLS)
                if num < 0:
                    num = num + len(self.SYMBOLS)

                # Add encrypted/decrypted number's symbol to translated:
                translated = translated + self.SYMBOLS[num]
            else:
                # Just add the symbol without encrypting/decrypting:
                translated += symbol

        return translated

    def hack(self, message: str):
        # Loop through every possible key.
        for key in range(len(self.SYMBOLS)):
            translated = ''

            # Decrypt each symbol in the message:
            for symbol in message:
                if symbol in self.SYMBOLS:
                    # Get the number of the symbol.
                    num = self.SYMBOLS.find(symbol)
                    num -= key  # Decrypt the number.

                    # Handle the wrap-around if num is less than 0:
                    if num < 0:
                        num += len(self.SYMBOLS)

                    # Add decrypted number's symbol to translated:
                    translated = translated + self.SYMBOLS[num]
                else:
                    # Just add the symbol without decrypting:
                    translated = translated + symbol

            # Display the key being tested, along with its decrypted text:
            print('Key #{}: {}'.format(key, translated))


if __name__ == "__main__":
    print('*** Caesar Cipher ***')
    print('The Caesar cipher encrypts letters by shifting them over by a')
    print('key number. For example, a key of 2 means the letter A is')
    print('encrypted into C, the letter B encrypted into D, and so on.')
    print()

    caeser_cipher = CaeserCipher()
    mode = caeser_cipher.mode
    key = caeser_cipher.key

    # Let the user enter the message to encrypt/decrypt:
    print(f'Enter the message to {mode}.')

    message = caeser_cipher.message

    translated = caeser_cipher.translate(mode=mode, key=key, message=message)

    # Display the encrypted/decrypted string to the screen:
    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard.')
    except:
        pass  # Do nothing if pyperclip wasn't installed.

    # Let the user specify the message to hack:
    print('Enter the encrypted Caesar cipher message to hack.')
    # encrypted = caeser_cipher.message
    caeser_cipher.hack(translated)
