
# Celine Hui - encode function

def encode(password):
    encoded = ""
    for num in password:
        num = int(num)
        if num >= 7:
            encoded += str(num - 7)
        else:
            encoded += str(num + 3)
    return encoded

# updated decode function
def decode(password):
    decoded = ""
    for num in password:
        num = int(num)
        if num <= 2:
            decoded += str(num + 7)
        else:
            decoded += str(num - 3)
    return decoded

while True:
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = int(input("Please enter an option: "))


    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored! ")
    elif option == 2:
        decoded_password = decode(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
    elif option == 3:
        break