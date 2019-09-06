# steam_library_comparision

This little python script allows you to compare your steam library with your friends but it does require some manual data collection.

### Instructions
1. Download/clone this project then delete the sample data from the "data" folder. 

2. Go to the stream profile page of the person(people) that you would like to compare with. On the right go to their "Games" page.
3. Right click on the page and "inspect" it. 
4. Use ctrl-f to find, inside of the page source, the "#games_list_row_container". 
5 Right click on it in the source and "Copy"->"Copy-element".
6. Save the copied list to an html file in the "data" folder.
7. Then from the command line or terminal run the python script. 'python process.py'
8. Your results should pop out in a "results.txt" file in right next to the script file.

### Dependencies
There is currently only one dependency, Beautiful Soup 4 (and python of course). Installation instructions can be found here https://www.crummy.com/software/BeautifulSoup/bs4/doc/ . 
