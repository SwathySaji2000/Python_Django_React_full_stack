
import re

license = "my car number is kl05am5962"

pattern = r'kl[0-9]{2}[a-z]{1,2}[0-9]{4}'  # r is used for check the  group

matcher = re.finditer(pattern,license)

for i in matcher:
    print(i.start(),i.end())