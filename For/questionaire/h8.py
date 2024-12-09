# 3. Reverse Words in a Sentence

# Given a sentence, reverse each word individually using a for loop.

# Example:
# Input: "Python is fun"
# Output: "nohtyP si nuf"


text = input("Enter the text: ")

rev_sen = ""

rev_word = ""

i = 0

for i in range (len(text)):

    if [text] != '':

      rev_word = text[i]

    else:  
       
       if rev_word:
          
          rev_sen += rev_word[::-1] + ' '

          rev_word = " "

if rev_word:

   rev_sen += rev_word[::-1]          


print(rev_sen)


