while True:
    User_Input = input("Enter your preferred sentence or word. '0' Exit ")
    if User_Input != "0":
        while True:
            User_Section = int(input("""Choose an Operation: 
            1. Reverse the sentence
            2. Count vowels
            3. Check if palindrome
            4. Find and replace a word
            5. Format (title case)
            6. Split into words
            7. Word frequency counter
            8. Swap case
            9. Exit 
            """))
            match User_Section:
                case 1:
                    print(User_Input[::-1])
                case 2:
                    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
                    Find = sum(1 for ch in User_Input if ch in vowels)
                    print("Number of Vowels: ",Find)
                case 3:
                    if User_Input == User_Input[::-1]:
                        print("Yes")
                    else:
                        print("No")
                case 4:
                    Select_word = input("What word would you like to replace? ")
                    Change_word = input("Enter word for replace: ")
                    Replace_word = User_Input.replace(Select_word, Change_word)
                    print(Replace_word)
                case 5:
                    Title_case = User_Input.title()
                    print(Title_case)
                case 6:
                    Split_Result = User_Input.split()
                    print(Split_Result)
                case 7:
                    from collections import Counter
                    words = User_Input.lower().split()
                    word_count = Counter(words)
                    print("Result: ")
                    for word, count in word_count.items():
                        print(f"{word}: {count}")
                case 8:
                    Swap_case = User_Input.swapcase()
                    print(Swap_case)
                case 9:
                    print("//Operation Close//")
                case _:
                    print("Invalid Choice, try again")
            if User_Section == 9:
                break
    elif User_Input == "0":
        print("///Exit///")
        break
