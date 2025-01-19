# wap for pancard validation

# caps alpha = 5

#  digits = 4

# apha = 1 

import re


text ="PLTPS9045L"
pattern = r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}'

matcher = re.findall(pattern,text)

print(matcher)