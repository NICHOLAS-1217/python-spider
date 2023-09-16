from bs4 import BeautifulSoup

with open('base.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('li')
    print(tags)