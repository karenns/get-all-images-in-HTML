# Library
import pandas as pd
import bs4 
#from urllib.parse import urlsplit

# Open CSV
df = pd.read_csv('input.csv', header=None)

# Get rid of all columns except the post_content
df = df[4]

# Make it smaller just for TESTING purposes
#df = df.loc[1:10]

# Open and clean the output file
file = open('output.txt', 'r+')
file.truncate(0) 


# Get only images
def show_imgSRC(html):
    file = open('output.txt', 'a')
    soup = bs4.BeautifulSoup(html, "html.parser")
    
    for img in soup.find_all('img'):
        output = [ img['src'],'\n']
        file.writelines(output)
        
    file.close()

# From each row - Get all images
df.apply(show_imgSRC)
