import re

html = '<a href="http://www.google.com">Google</a>'

pattern = r'<a href="(.+?)">(.+?)</a>'
match = re.search(pattern, html)
if match:
    print(match.group(1))
    print(match.group(2))
    print(f"Link: {match.group(1)}, Text: {match.group(2)}")

