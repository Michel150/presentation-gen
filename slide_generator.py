import write_slideshow
import download_wikipage
import sys
from lxml import etree

def generate_title_page(title, html_tree):
    img_link = html_tree.xpath("(//a[@class='image'])[2]")
    if(len(img_link) < 1):
        print(f"No picture found -> cannot create title page")
        return None
    href = img_link[0].attrib['href']
    pic_name = download_wikipage.download_original_image(href)

    return write_slideshow.title_slide(title, pic_name)

def generate_contents(html_tree):
    content_element = html_tree.xpath("//div[@id='toc']")
    if(len(content_element) != 1):
        print(f"Didnot find exactly on toc, but {len(content_element)}")
        return ""
    contents = content_element[0].xpath("./ul/li/a/span[@class='toctext']/text()")
    number_of_elements = contents.index("See also")

    points_text = "<ul>"
    for point in contents[:number_of_elements]:
        points_text += f"<li>{point}</li>"
    points_text += "</ul>"
    return write_slideshow.text_slide("Contents", points_text)

if len(sys.argv) != 2:
    print("requires wikipedia title as first argument")
    sys.exit(1)

title = sys.argv[1]

wiki_page = etree.HTML(download_wikipage.download(title))
slides = []

slides.append(generate_title_page(title=title, html_tree=wiki_page))
slides.append(generate_contents(html_tree=wiki_page))

write_slideshow.write_slides(slides)