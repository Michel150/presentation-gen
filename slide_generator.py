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

if len(sys.argv) != 2:
    print("requires wikipedia title as first argument")
    sys.exit(1)

title = sys.argv[1]

wiki_page = download_wikipage.download(title)

# slides.append(generate_title_page(title=title, html_tree=html_tree))

# pip install wikipedia_sections
sections_full = wiki_page.sections
sections = sections_full[:sections_full.index("See also")]
print(sections)

sections_c = [wiki_page.section(s) for s in sections]
print(sections_c)

# toc = generate_contents(html_tree)
# points_text = "<ul>"
# for point in toc:
#     points_text += f"<li>{point}</li>"
# points_text += "</ul>"
# slides.append(write_slideshow.text_slide("Contents", points_text))

# paragraphs = get_paragraph_texts(html_tree, len(toc))
# print(paragraphs[0])

# write_slideshow.write_slides(slides)