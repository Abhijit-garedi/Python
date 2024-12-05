# simple progrm that show the big bracket in regex
import re
print(re.findall(r"[aeiou]", "Regex is fun!"))
# Output: ['e', 'e', 'i', 'u']
