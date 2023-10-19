import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

"""
This script is used to convert the xml file from the following link to images:
https://data.gov.il/dataset/tqhe
The script expect to be in the same directory as the xml file and the font file.
"""
def main():
    font_absolute_path = "VarelaRound-Regular.ttf"
    font_size = 36

    tree = ET.parse("./TheoryExamHE-DATA.xml")

    items = tree.findall('./channel/item')
    for item in tqdm(items):
        question = ""
        answers = []
        for sub_item in item:
            if sub_item.tag == 'title':
                question = sub_item.text

            if sub_item.tag == "description":
                html = ET.fromstring(sub_item.text)
                li = html.findall("./ul/li/span")
                for l in li:
                    answers.append(l.text)

        image = Image.new("RGB", (1920 , 1080), (200, 200, 200))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_absolute_path, font_size)
        draw.text((0, 50), fill_for_align_right(question), font=font, fill=(0, 0, 0))
        answerY = 240

        for i in range(0, len(answers)):
            draw.text((10, answerY + i * 160), fill_for_align_right(answers[i]), font=font, fill=(0, 0, 0))

        image.save("q" + question[:4] + ".jpg", "JPEG")


def fill_for_align_right(text):
    return text + " " * (90 - len(text))


if __name__ == "__main__":
    main()
