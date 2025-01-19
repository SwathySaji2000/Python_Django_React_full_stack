import re

# find the matching of words starts with capital letters



text = "Python is a Programming_language"

pattern = r'\b[A-Z][a-z]*'  #['Python', 'Programming']
#pattern = r'\b[A-Z][a-z]*\b' #['Python']


# defines * which takes all characters start with caps and small ,\b which defines begining of the word

matcher = re.findall(pattern,text)

print(matcher)