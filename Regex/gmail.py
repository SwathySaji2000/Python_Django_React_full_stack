import re

# wap to validate mail id

text = "swathysaji123@gmail.com"

pattern = r'\b[A-z0-9#]+@[a-z]*+.[a-z]{2,}\b'  # we can include in a group A-Z a-z special characters that can enroll as you want ,, * for repeating
# 

match = re.findall(pattern,text)

print(match)