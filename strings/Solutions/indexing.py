def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep="")
    pos = int(input("Which character would you like to see? [Enter number] "))
    print("Character number", pos, "is", phrase[pos])

main()