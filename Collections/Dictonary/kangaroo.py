
# wap to check whether is a kangaroo or not


text = "observe"

word = "serve"

w_c = {}

for i in word:

    w_c[i] = word.count(i)  

print(w_c)    


for chr in text:

    if (chr in w_c) and w_c[i] > 0:
        w_c[chr] -=1

    else:
        print("not a kangaroo")
        break    

else:
    print(f"{text} is a kangaroo")    