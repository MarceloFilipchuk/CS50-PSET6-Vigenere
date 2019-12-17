import sys


def main():

    if len(sys.argv) != 2 or sys.argv[1].isalpha() == False:
        print("Usage: ./vigenere keyword")
        sys.exit(1)

    key = sys.argv[1]
    counter = 0
    plaintext = input("plaintext: ")
    print("ciphertext: ", end="")

    # Iterates over the plaintext changing each character according to the key and printing it
    for c in plaintext:
        # Checks if the character is an alphabetic
        if c.isalpha():
            k = keyword(key[counter])
            # Checks whether the character is an uppercase or lowercase one
            if c.islower():
                c = chr(ord(c) + k)
                while ord(c) > 122:
                    c = chr(97 + ord(c) % 123)
            elif c.isupper():
                c = chr(ord(c) + k)
                while ord(c) > 90:
                    c = chr(65 + ord(c) % 91)
            counter += 1
            if counter == len(key):
                counter = 0
            print(c, end="")
        # The character is not an alphabetic, thus it prints it as it is
        else:
            print(c, end="")
    print()
    return 0


# Returns the correspondant key according to the current char that is passed
def keyword(c):
    return (ord(c.lower()) % 97)


if __name__ == "__main__":
    main()

