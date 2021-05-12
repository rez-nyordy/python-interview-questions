# Question #6
# If this code were run, what would the output to the console?

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
<head>
<title>Cats!</title>
</head>
<body>
    <h1>Sphinx</h1>
    <p>The sphinx is a breed of cat that is completely hairless.</p>
    <p>This cat's name is Harold.</p>
    <p>Harold is a good kitty.</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
p_tags = soup.find_all('p')

print(len(p_tags))
