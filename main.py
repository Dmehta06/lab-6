#Dipak Mehta 

def encode(password):
    encoded_password = ""
    for x in password:
        for _ in range(3):
            if x == "9":
                x = "0"
            else:
                x = str(int(x) + 1)
        encoded_password = encoded_password + x
    return encoded_password


def decode(password):
    decoded_password = ""
    for x in password:
        for _ in range(3):
            if x == "0":
                x = "9"
            else:
                x = str(int(x) - 1)
        decoded_password += x
    return decoded_password


if __name__ == "__main__":
    while True:
        print("1. Encode")
        print ("2. Decode")
        selection = int(input("Menu Selection: "))

        if selection == 1:
            print(f"\nEncoded Password: {encode(input("Password: "))}")
        elif selection == 2:
            print(f"\nDecoded Password: {decode(input("Password: "))}")
        else:
            print("Invalid Selection")
