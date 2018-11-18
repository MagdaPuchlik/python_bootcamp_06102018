import re

pattern=re.compile("\d{3}-\d{2,3}-\d{3}")

text = "122-233-344"
print(pattern.findall(text))