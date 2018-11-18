from requests import get
# get to jedna z metod http (wykonywana jest zawqsze gdy wpiosujmey coś w okno przeglądarki)

from bs4 import BeautifulSoup

old=[
    "Programming Computer Vision with Python. Tools and algorithms for analyzing images",
    "Programming Python. Powerful Object-Oriented Programming. 4th Edition",
    "Real World Instrumentation with Python. Automated Data Acquisition and Control Systems",
    "Bioinformatics Programming Using Python. Practical Programming for Biological Data",
    "Head First Programming. A learner's guide to programming using the Python language",
    "Natural Language Processing with Python",
    "Python for Unix and Linux System Administration",
    "Learning Python. 3rd Edition",
    "Regular Expression Pocket Reference. Regular Expressions for Perl, Ruby, PHP, Python, C, Java and .NET. 2nd Edition",
    "Programming Python. 3rd Edition",
    "Python in a Nutshell. 2nd Edition",
    "Learning Python. 2nd Edition",
    "Python & XML. XML Processing with Python"
]


url="https://helion.pl/kategorie/programowanie/python"
response = get(url)

# print(response.text) #drukowany jest kod [200] który oznacza że wszytko poczło pomyslnie

# response.text = pokąz źródło strony, pokazuje kod tworzący stronę
html_soup = BeautifulSoup(response.text,'html.parser')

books = html_soup.find_all('div',class_="book-info")

nowe = set()
for b in books:
    nowe.add(b.a.text)

    print(nowe-old)

# do doczytania z zajęć , porówananie list, wersji