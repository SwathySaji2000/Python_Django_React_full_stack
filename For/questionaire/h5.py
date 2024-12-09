# Given a string, count the frequency of each character using a for loop and display the results.


text = input("Enter a word: ")


for i in text:

    if text.index(i) == text.find(i):

        count = 0

        for c in text:

            if c == i:

                count += 1

        print(f"{i}:{count}")        










