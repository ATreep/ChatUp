import logging

from functions.engine import Engine
from spacy.tokens import Doc
import crawler
import jieba
import jieba.posseg as pseg
from xpinyin import Pinyin
import json

jieba.setLogLevel(logging.INFO)

p = Pinyin()


class WeatherEngine(Engine):
    purpose = "查看天气预报"

    def __init__(self, doc: Doc):
        super().__init__(doc)

        try:
            location = "beijing"
            location_cn = "北京市"

            words = pseg.cut(doc.text)

            for word, pos in words:
                if pos == "ns":
                    location = p.get_pinyin(word.replace("市", "")).replace("-","")
                    location_cn = word.replace("市", "") + "市"

            api_result = crawler.api_response(
                    f"https://api.seniverse.com/v3/weather/daily.json?key=S597iQ10_nzJdwoOt&location={location}&language=zh-Hans&unit=c&start=0&days=5").text

            api_dict = json.loads(api_result)
            api_list = api_dict['results'][0]['daily']
            weathers_list = []

            for obj in api_list:
                weathers_list.append((obj['date'], obj['text_day'], obj['text_night']))

            self.output_text += f"好的，这是 {location_cn} 未来 {len(weathers_list)} 天的天气情况：\n"

            for day_weather in weathers_list:
                self.output_text += f"{day_weather[0]} 日，白天 {day_weather[1]}，夜间 {day_weather[2]}。\n"

        except:
            self.output_text = "抱歉，我无法获取天气信息。"
