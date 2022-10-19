import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

def serch_cat(name):

    search = name
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
    newUrl = url + quote_plus(search) +'%20기본정보'

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    data = requests.get(newUrl,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    datas = soup.select('#main_pack > div.sc_new.cs_common_module.case_normal.color_15._pet > div.cm_content_wrap > div > div > div.detail_info >div')

    infos = soup.select('#main_pack > div.sc_new.cs_common_module.case_normal.color_15._pet > div.cm_content_wrap > div > div > div.detail_info > dl > div')

    imgs = soup.select('#main_pack > div.sc_new.cs_common_module.case_normal.color_15._pet > div.cm_content_wrap > div > div > div.detail_info > span')

    if not datas or not infos or not imgs:  
        search = name
        url = 'https://www.google.com/search?q='
        newUrl = url + quote_plus(search)
        output_data = {
            'none' : True,
            'name' : name,
            'url' : newUrl,
        }

        return output_data

    else:
        for data in datas:
            text = data.select_one('span').text
    
        for img in imgs:
            img_src = img.select_one('img')['src']
        
        total_info = []
        for info in infos:
            tage_data = info.select_one('dt').text
            info_data = info.select_one('dd').text
            input_data = tage_data + ' : ' + info_data
            total_info.append(input_data)
        
        output_data = {
            'none' : False,
            'name' : name,
            'info' : total_info,
            'text' : text,
            'img' : img_src,
        }
        return output_data