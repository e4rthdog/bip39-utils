import sys

def encode(word, string):
    result = ""
    for char in string:
        try:
            index = word.index(char)
            result += str(index)
        except ValueError:
            result += " "  # Replacing underscore with space
    return result

def decode(word, number_string):
    result = ""
    for num in number_string:
        try:
            index = int(num)
            if index < len(word):
                result += word[index]
            else:
                result += " "  # Replacing underscore with space
        except ValueError:
            result += " "  # Replacing underscore with space
    return result

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py -e/-d <word> <string/number_string>")
        sys.exit(1)

    mode = sys.argv[1]
    word = sys.argv[2]
    input_string = sys.argv[3]

    if mode == "-d":
        result = encode(word, input_string)
    elif mode == "-e":
        result = decode(word, input_string)
    else:
        print("Invalid mode. Use -e for decode or -d for encode.")
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()
