from bs4 import BeautifulSoup
import requests
import urllib.request
import os
#Does the path exist
if os.path.exists("images/") == False:
    os.mkdir("images/")


# This url will change at each increment.
active = True
comicNum = 401
url = "https://chiefobrienatwork.com"
while active:
    found = False   
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    #find the button that links to the previous episode
    links = soup.find_all('a')
    imgs = soup.find_all("img")
    imgToDraw = imgs[1].attrs['src']
    #Get the name of the comic
    text = soup.find('div',{"class": "caption"})
    text2 = text.find("p")
    if text2.decode_contents() == "<br/>":
        text2 = text2.find_next("p")
    text2 = text2.decode_contents().replace(":", '').replace("<br/>","").replace("?", "")
    #kickstarter usecases I guess
    if "kickstarter" in text2:
        text2 = "kickstarterComic"
    print(text2)
    urllib.request.urlretrieve(imgToDraw, "images/" + "({}) ".format(comicNum) + text2 + ".jpg")
    for link in links:
        if link.get_text() == "Previous":
            url = "https://chiefobrienatwork.com" + link.attrs['href']
            #usecase of weird url
            comicNum -= 1
            found = True
    if found == False:
        active = False
print("It is finished.")
