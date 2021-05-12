# Question #5
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
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
text = soup.find_all('p')[1].get_text()

print(text)
