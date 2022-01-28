import requests
from lxml import etree
import shutil
import wikipedia

session = requests.Session()

def download(name, language = "en"):
    wikipedia.set_lang(language)
    print(f"looking up page for '{name}'")
    query_r = wikipedia.suggest(name)
    print(f"suggested as '{query_r}'")
    return wikipedia.page(title=query_r)

def download_original_image(link):
    url = f'https://wikipedia.org{link}'
    tree = etree.HTML(session.get(url).content)
    a_e = tree.xpath("//a[text()='Original file']")
    pic_url = f"https:{a_e[0].attrib['href']}"
    name = pic_url.split('/')[-1]
    r = session.get(pic_url, stream=True)
    if r.status_code == 200:
        with open(f"./my_slideshow/{name}", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)     
    return name
