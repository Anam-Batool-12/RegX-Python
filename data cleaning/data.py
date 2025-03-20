import re
text = "This   is   a   test   string"
text = text.strip()
pattern = r'\s+'
text = re.sub(pattern, ' ', text)
print(text)
