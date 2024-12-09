# 5. Remove Duplicates

# Write a program to remove all duplicate characters in the string.


text = input("Enter the text: ")

rec = ""

for i in text:

    if i not in rec:
        rec += i

print(f" string after removing recursive characters:{rec}")        