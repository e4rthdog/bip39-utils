import sys
from mnemonic import Mnemonic

def get_word_indices(mnemonic_phrase):
    # Initialize the BIP-39 word list
    mnemo = Mnemonic("english")
    
    # Split the mnemonic phrase into individual words
    words = mnemonic_phrase.split()

    # Check if the number of words is valid (12, 18, or 24)
    if len(words) not in [12, 18, 24]:
        return "Invalid number of words. Must be 12, 18, or 24."

    # Get the word indices with zero-padding
    indices = []
    for word in words:
        index = mnemo.wordlist.index(word) + 1
        padded_index = str(index).zfill(4)  # Pad with zeros to ensure length of 4
        indices.append(padded_index)

    return indices

def get_word_from_indices(indices):
    # Initialize the BIP-39 word list
    mnemo = Mnemonic("english")

    # Get words from indices
    words = []
    for index in indices:
        word = mnemo.wordlist[int(index) - 1]  # Convert back to integer
        words.append(word)

    return words

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py -n|-w [-l] 'mnemonic_phrase or space-separated indices'")
        sys.exit(1)

    flag = sys.argv[1]
    output_as_list = "-l" in sys.argv
    mnemonic_phrase = sys.argv[-1]

    if flag == "-n":
        word_indices = get_word_indices(mnemonic_phrase)
        if output_as_list:
            for index in word_indices:
                print(index)
        else:
            print(" ".join(word_indices))  # Already formatted
    elif flag == "-w":
        try:
            indices = [index.zfill(4) for index in mnemonic_phrase.split()]  # Ensure padding
            words = get_word_from_indices(indices)
            if output_as_list:
                for word in words:
                    print(word)
            else:
                print(" ".join(words))
        except ValueError:
            print("Invalid input for word indices. Use space-separated integers.")
    else:
        print("Invalid flag. Use -n to convert words to numbers or -w to convert numbers to words.")
