import requests
from bs4 import BeautifulSoup

def get_chess_puzzles(dir):
    res = requests.get(url="https://www.reddit.com/r/chess?f=flair_name%3A%22Puzzle%2FTactic%22",headers={'Content':'text/html','User-Agent':'firefly'})
    soup = BeautifulSoup(res.content, "html.parser")
    imgs = soup.find_all("img")
    print(len(imgs))
    for i,img in enumerate(imgs):
    print(img['src'])
    if 'preview.redd' in img['src']:
        imgfile = requests.get(url=img['src'],headers ={'Content':'image/png','User-Agent':'firefly'})
        with open(f'chess_puzzle{i}.png','wb+') as file:
            file.write(imgfile.content)
