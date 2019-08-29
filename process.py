# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


from bs4 import BeautifulSoup
import os

def parse():
    path = 'data/'
    folder = os.fsencode(path)
    users_games = []

    # Go through each html file and strip the titles
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.html') ):
            with open(path + filename) as fp:
                soup = BeautifulSoup(fp, features='lxml')
            your_rows = soup.find_all(class_='gameListRowItemName')
            game_titles = []
            for game in your_rows:
                game_titles.append(game.text)
            users_games.append(game_titles)
    
    # Merge the lists by intersection
    intersect = users_games[0]
    for title_list in users_games:
        intersect = intersection(intersect, title_list)

    # Save the file
    with open('results.html', 'w') as f:
        for item in intersect:
            f.write(str("%s\n" % item))
    
def intersection(list1, list2):
    temp_list = []
    for item in list1:
        if item in list2:
            temp_list.append(item)
    return temp_list

parse()