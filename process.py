# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


from bs4 import BeautifulSoup
import os

compiled_list = {}

def parse():
    path = 'data/'
    folder = os.fsencode(path)
    users_games = []

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
            users_games.append(game_titles)
    
    counts = [[] for i in range(num_players)]
    for game_name, count in compiled_list.items():
        counts[count].append(game_name)

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
    
def intersection(list1, list2):
    temp_list = []
    for item in list1:
        if item in list2:
            temp_list.append(item)
    return temp_list

parse()