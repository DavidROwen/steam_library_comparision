# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import os

def parse():
    path = 'data/'
    folder = os.fsencode(path)
    compiled_list = {}

    # Go through each html file and strip the titles
    num_players = len(os.listdir(folder))
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.html') ):
            with open(path + filename) as fp:
                soup = BeautifulSoup(fp, features='lxml')
            your_rows = soup.find_all(class_='gameListRowItemName')
            game_titles = []
            for game in your_rows:
                game_titles.append(game.text)
                if game.text in compiled_list:
                    compiled_list[game.text] -= 1
                else:
                    compiled_list[game.text] = num_players - 1
    
    # Split games into lists based on how many of the players do not own them
    counts = [[] for i in range(num_players)]
    for game_name, count in compiled_list.items():
        counts[count].append(game_name)

    # Alphabetically sort the lists of games
    for category in counts:
        category.sort()

    # Save the file
    with open('results.txt', 'w') as f:
        i = 0
        for games in counts:
            f.write(str("\n-#- %i players would need to buy these games -#-\n" % i))
            for game in games:
                f.write(str("%s\n" % game))
            i += 1

parse()