from functions.engine import Engine
from spacy.tokens import Doc
import crawler
from bs4 import BeautifulSoup
from lxml import etree


class WikiEngine(Engine):
    purpose = "搜索百科"

    def __init__(self, doc: Doc):
        super().__init__(doc)

        try:
            reserve_key_noun = ["信息", "百科", "身份", "定义"]
            keywords = []

            for word_doc in doc:
                if word_doc.pos_ == "NOUN" or word_doc.pos_ == "PROPN":
                    if word_doc.text not in reserve_key_noun:
                        keywords.append(word_doc.text)

            keywords = list(set(keywords))

            if len(keywords) > 1:
                self.output_text += "你想要知道有关下列哪一项的信息？\n"
                for word in keywords:
                    self.output_text += "• " + word + "\n"

                self.output_text += "请更加简明准确地告诉我你想要了解的对象。"
                return

            # Parse web code.

            url = "https://baike.baidu.com/item/" + keywords[0]

            wiki_url = url

            web_code = crawler.web_content(url)

            soup = BeautifulSoup(web_code, features="lxml")

            subLemmaListTitleList = soup.find_all(name='div', attrs={'class': 'lemmaWgt-subLemmaListTitle'})

            if len(subLemmaListTitleList) > 0:
                subLemmaListTitle = subLemmaListTitleList[0].text.strip()
                wiki_url = url
                if subLemmaListTitle.startswith("这是一个多义词，请在下列义项上选择浏览"):
                    self.output_text += "这是一个多义词。我下面为你查找到的是最常用的一个义项 "
                    multiple_meaning_li = soup.find_all(name='ul', attrs={'class': 'custom_dot para-list list-paddingleft-1'})[0]
                    multiple_names_and_links = []
                    for li in multiple_meaning_li.children:
                        if li.text.strip() == "":
                            continue

                        multiple_names_and_links.append((li.text.strip(), list(list(li.children)[1].children)[1]["href"]))

                    self.output_text += multiple_names_and_links[0][0] + "。\n"

                    wiki_url = "https://baike.baidu.com" + multiple_names_and_links[0][1]

            details_web_code = crawler.web_content(wiki_url)

            intro = "".join(etree.HTML(details_web_code).xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]/text()"))

            self.output_text += intro
        except:
            self.output_text = "抱歉，我无法获取相关百科信息。"


