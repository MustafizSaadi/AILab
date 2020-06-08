while True:
    string =input("Enter On for Online mode or Off for Offline mode or exit to quit the program\n")
    if string.lower() == "off":
        exec(open("Offline.py").read())
    elif string.lower() == "on":
        exec(open("Online.py").read())
    elif string.lower() == "exit":
        break
    else:
        print("Please follow the instruction\n")