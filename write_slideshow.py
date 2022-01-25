image_template = None
title_template = None
text_template = None
idx_template = None

def init_templates():
    global image_template
    global title_template
    global text_template
    global idx_template

    with open("slideshow_template/image_template.html","r") as f:
        image_template =  f.read()
    with open("slideshow_template/title_template.html","r") as f:
        title_template =  f.read()
    with open("slideshow_template/text_template.html","r") as f:
        text_template =  f.read()
    with open("slideshow_template/index_template.html","r") as f:
        idx_template =  f.read()

init_templates()

class image_slide:
    def __init__(self, caption, image_url):
        self.caption = caption
        self.image_url = image_url

    def create_slide(self, page_number, total_pages):
        return image_template.format(page_number, total_pages, self.image_url, self.caption)

class title_slide:
    def __init__(self, title, image_url):
        self.title = title
        self.image_url = image_url

    def create_slide(self, page_number, total_pages):
        return title_template.format(page_number, total_pages, self.image_url, self.title)

class text_slide:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def create_slide(self, page_number, total_pages):
        return text_template.format(page_number, total_pages, self.title, self.content)

def write_slides(slides):
    slideshow = ""
    for i, s in enumerate(slides):
        slideshow += f"{s.create_slide(i + 1, len(slides))}\n"
    idx_text = idx_template.format(slideshow)
    with open("my_slideshow/index.html", "w") as f:
        f.write(idx_text)