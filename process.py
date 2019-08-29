# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import os

def parse():
    path = 'data/'
    folder = os.fsencode(path)
    rows = []

    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.html') ):
            with open(path + filename) as fp:
                soup = BeautifulSoup(fp, features='lxml')
            # print(soup.prettify())
            # print(soup.find_all(class_='gameListRow'))
            your_rows = soup.find_all(class_='gameListRowItemName')
            # print(your_rows)
            titles = []
            for row in your_rows:
                titles.append(row.text)
            # print(titles)
            rows.append(titles)
    
    intersect = rows[0]
    # print(rows)
    for title_list in rows:
        # print(title_list)
        intersect = intersection(intersect, title_list)
    
    # print(intersect)

    f = open('results.html', 'w')
    for item in intersect:
        f.write(str("%s\n" % item))
    f.close()
    # print(intersect)

# def row_finder(tag):
#     return tag.has_attr('class') and 

def intersection(lst1, lst2):
    # print(lst1) 
    temp_list = []
    for item1 in lst1:
        if item1 in lst2:
            temp_list.append(item1)
    return temp_list

parse()