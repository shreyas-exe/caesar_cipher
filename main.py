from art import alphabet,logo


def caesar(opr: str, text: str, shift_code: int):
    produced_text = ""

    for i in text:
        if opr == "encode":
            index = alphabet.index(i) + shift_code
        else:
            index = alphabet.index(i) - shift_code
        temp_chr = alphabet[index]
        produced_text += temp_chr
    return produced_text


if __name__ == "__main__":
    print(logo)
    ch = 'y'
    while ch == 'y':
        opr = input(
            "what operation do you have to perform?\n-> Encode\n-> Decode\n"
        ).lower()

        if opr not in ("encode","decode"):
            print("try again, seems like you've chose a wrong option :/")
            quit()
        else:
            text = input("Type out the text here:").lower()
            shift_code = int(input("Enter the Shift code:"))
            print(caesar(opr, text, shift_code))
        ch = input("do you want to continue?\ny for yes, n for no\n").lower()
        
