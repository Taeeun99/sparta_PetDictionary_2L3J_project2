import requests
from bs4 import BeautifulSoup


## 세팅
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
dog_data = requests.get('https://mypetlife.co.kr/dog-lab',headers=headers)
cat_data = requests.get('https://mypetlife.co.kr/cat-lab',headers=headers)

soup_dog = BeautifulSoup(dog_data.text, 'html.parser') # data.text파일을 html.parser을 통해 html 문법으로 정돈
soup_cat = BeautifulSoup(cat_data.text, 'html.parser') # data.text파일을 html.parser을 통해 html 문법으로 정돈

########################################################
print(soup_dog.prettify()) #출력물에 공백 추가하여 보기좋게 변환
print(soup_dog.select('title'))


#main-content-row > div > div.hide-scroll.popular-posts > div.popular-post-grid.post_id-39451 > span.post-thumbnail > a > img
#main-content-row > div > div.hide-scroll.popular-posts > div.popular-post-grid.post_id-112731 > span.post-thumbnail > a > img


#main-content-row > div > div.hide-scroll.popular-posts > div.popular-post-grid.post_id-
#> span.post-thumbnail > a > img




