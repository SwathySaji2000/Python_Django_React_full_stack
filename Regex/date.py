import re 

# wap to find the date format

text = " hello 01-03-2025"

pattern = r'\b(0[0-9]|1[0-9]|2[0-9]|3[0-2])-(0[1-9]|1[1-2])-(\d{4})'

match = re.findall(pattern,text)

print(match)
            

            




