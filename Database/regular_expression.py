import re

# Sample text
text = "Contact us at support@agri.com or sales@Nargroup.org."

# Regular expression to find email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all matches
emails = re.findall(pattern, text)

print("Found email addresses:", emails)

# Output
# Found email addresses: ['support@agri.com', 'sales@Nargroup.org']
