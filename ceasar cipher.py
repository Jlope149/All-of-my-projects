
def ceasar_shift(message,shift):
    result = ""
    FIRST_CHAR_CODE = ord("A")
    LAST_CHAR_CODE = ord("Z")
    CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1
    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char
    return result

message = str(input("Enter What You Want To Be Ciphered: "))
shift = int(input("Enter Shift Amount: (Integer) "))

print(f"Ciphered Version: {ceasar_shift(message,shift)}")