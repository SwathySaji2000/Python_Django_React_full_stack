# wap to find the index and first occurence of the text

text = "helloworld"

target = "o"

for i in text:

    if i == target:

        print(text.index(i))

        break
else:

        print("not found")