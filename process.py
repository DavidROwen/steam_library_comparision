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
            your_rows = soup.find_all(class_='gameListRowItemName')
            titles = []
            for row in your_rows:
                titles.append(row.text)
            rows.append(titles)
    
    intersect = rows[0]
    for title_list in rows:
        intersect = intersection(intersect, title_list)

    f = open('results.html', 'w')
    for item in intersect:
        f.write(str("%s\n" % item))
    f.close()
    
def intersection(lst1, lst2):
    # print(lst1) 
    temp_list = []
    for item1 in lst1:
        if item1 in lst2:
            temp_list.append(item1)
    return temp_list

parse()