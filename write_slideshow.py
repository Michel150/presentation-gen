title_template = None
text_template = None
idx_template = None

def init_templates():
    global title_template
    global text_template
    global idx_template

    with open("libre_office/title_page.xml","r") as f:
        title_template =  f.read()
    with open("libre_office/text_page.xml","r") as f:
        text_template =  f.read()
    with open("libre_office/alizarin_template.fodp","r") as f:
        idx_template =  f.read()

init_templates()

class title_slide:
    def __init__(self, title, sub_title = ""):
        self.title = title
        self.sub_title = sub_title

    def create_slide(self, page_number):
        return title_template.format(self.title, self.sub_title)

class text_slide:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def create_slide(self, page_number):
        list_items = ""
        for c in self.content:
            list_items += f"<text:list-item> <text:p>{c}</text:p> </text:list-item>\n"
        return text_template.format(page_number, self.title, list_items)

def write_slides(slides):
    slideshow = ""
    for i, s in enumerate(slides):
        slideshow += f"{s.create_slide(i + 1)}\n"
    idx_text = idx_template.format(slideshow)
    with open("libre_office/my_slideshow.fodp", "w") as f:
        f.write(idx_text)