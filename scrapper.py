import requests
from bs4 import BeautifulSoup as bs
import os

url = "https://www.netflix.com/de-en/"


def getImages(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass

    os.chdir(os.path.join(os.getcwd(), folder))
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')
    images = soup.find_all('img')

    # add alt conditionals for file name
    x = 1
    for image in images:
        # alt = image['alt']
        link = image['src']
        name = "image {}".format(x)
        x += 1
        print(name, link)
        with open(name + '.jpg', 'wb') as file:
            imag = requests.get(link)
            file.write(imag.content)
            print("writing", name, " to the folder")


getImages(url, 'netflix')
