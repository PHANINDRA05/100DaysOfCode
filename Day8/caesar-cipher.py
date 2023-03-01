logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    def caesar(text, shift, direction):
        res_string = ""
        if direction == 'encode':
            for i in range(len(text)):
                ascii_of_newnum = ord(text[i]) + shift
                if ascii_of_newnum > 122:
                    ascii_of_newnum = 96 + (ascii_of_newnum - 122)
                res_string += chr(ascii_of_newnum)
        elif direction == 'decode':
            for i in range(len(text)):
                ascii_of_newnum = ord(text[i]) - shift
                if ascii_of_newnum < 97:
                    ascii_of_newnum = 123 + (ascii_of_newnum - 97)
                res_string += chr(ascii_of_newnum)
        print(res_string)
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("Invalid Direction")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != 'yes':
        break

# def decrypt(text,shift):
#     decrypted_string = ""
#     for i in range(len(text)):
#         ascii_of_newnum = ord(text[i]) - shift
#         if ascii_of_newnum < 97:
#             ascii_of_newnum = 123 + (ascii_of_newnum - 97)
#         decrypted_string += chr(ascii_of_newnum)
#     print(f"Here's the encoded result: {decrypted_string}")
#     print("Type 'yes' if you want to go again. Otherwise type 'no'.")
# def encrypt(text,shift):
#     encrypted_string = ""


