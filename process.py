# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup


soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())