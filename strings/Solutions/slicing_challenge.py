def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is '", phrase, "'", sep="")
    pos1 = int(input("Which character would you like to start with? [Enter number] "))-1
    pos2 = int(input("Which character would you like to end with? [Enter number] "))
    print("Your substring is '",phrase[pos1:pos2],"'",sep="")

main()