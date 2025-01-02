# wap to print the characterstics of a string in even positions.

text = "python"

for i in range (len(text)):

    if i % 2 == 0:

         print(f"Position {i}: {text[i]}")