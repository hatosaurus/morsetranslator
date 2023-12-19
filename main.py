code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.',
             'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',
             'S': '...', 'T': '-', 'U': '..-',
             'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..',

             '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..',
             '9': '----.',

             ' ': '/'
             }

dict_reversed = {value: key for key, value in code_dict.items()}


def to_morse():
    to_translate = input("Enter the text to translate to morse code: ").upper()
    translated = []
    for char in to_translate:
        if char in code_dict:
            morse = code_dict[char] + " "
            # print(f"The morse value of {char} is {code_dict[char]}")
            translated.append(morse)
        else:
            pass
            # print(f"The character {char} is not here.")
    output = ''.join(translated)
    print(output)


def from_morse():
    to_translate = input("enter the morse code to translate to text: ").upper()
    translated = []
    hold = ""
    for char in to_translate:
        if char == "/":
            space = " "
            # print(f"Word break detected with {char}.")
            translated.append(space)
        elif char != " ":
            # print(f"The character {char} has been added to hold.")
            hold += char
        else:
            if hold:
                text = dict_reversed.get(hold, "")
                translated.append(text)
                # print(f"A space was detected. {text} has been added to output. Hold is cleared.")
                hold = ""

    if hold:
        text = dict_reversed.get(hold, "")
        translated.append(text)
        # print(f"The last word was detected. {text} has been added to output. Hold is cleared.")

    output = ''.join(translated)
    print(output)


while True:
    selection = input("Translate TO Morse code or FROM Morse code? Type TO or FROM: ").upper()

    if selection == "TO":
        to_morse()
    elif selection == "FROM":
        from_morse()
    else:
        print("Invalid selection. Please type TO or FROM.")
        continue


