import write_slideshow
import download_wikipage
import text_summarizer
import sys

def generate_title_page(title, html_tree):
    img_link = html_tree.xpath("(//a[@class='image'])[2]")
    if(len(img_link) < 1):
        print(f"No picture found -> cannot create title page")
        return None
    href = img_link[0].attrib['href']
    pic_name = download_wikipage.download_original_image(href)

    return write_slideshow.title_slide(title, pic_name)

def load_sections(wiki_page, min_char_s = 500):

    # pip install wikipedia_sections
    sections_full = wiki_page.sections
    sections = sections_full[:sections_full.index("See also")]
    sections_c = [wiki_page.section(s) for s in sections]

    sections_f = []
    sections_c_f = []
    for i, s_c in enumerate(sections_c):
        print(len(s_c))
        if(len(s_c) >= min_char_s):
            sections_f.append(sections[i])
            sections_c_f.append(s_c)
    return sections_f, sections_c_f


if len(sys.argv) != 2:
    print("requires wikipedia title as first argument")
    sys.exit(1)

title = sys.argv[1]

slides = [write_slideshow.title_slide(title=title)]

wiki_page = download_wikipage.download(title)
titles, sections = load_sections(wiki_page=wiki_page)
for i, t in enumerate(titles):
    sec_sum = text_summarizer.summarize(sections[i], num_sntnc=5)
    slides.append(write_slideshow.text_slide(t, sec_sum))

write_slideshow.write_slides(slides)