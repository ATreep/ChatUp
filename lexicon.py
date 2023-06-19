import spacy
from spacy.tokens import Doc
from functions.engine import Engine
from functions.mathematics_solver_engine import MathematicsSolverEngine
from functions.wiki_engine import WikiEngine
from functions.weather_engine import WeatherEngine
import utils


class Bridge:
    def __init__(self, noun_list: list, verb_list: list, pron_list: list, engine_type: type):
        self.noun_list = noun_list
        self.verb_list = verb_list
        self.pron_list = pron_list
        self.engine_type = engine_type

    def match(self, sentence_doc: Doc) -> float:
        score = 0
        for word in sentence_doc:
            if word.pos_ == "VERB":
                for verb in self.verb_list:
                    score += 1 if verb == word.text else utils.get_similarity(word.text, verb)

            if word.pos_ == "NOUN" or word.pos_ == "PROPN":
                for noun in self.noun_list:
                    score += 1 if noun == word.text else utils.get_similarity(word.text, noun)

            if word.pos_ == "PRON":
                for pron in self.pron_list:
                    score += 1 if pron == word.text else utils.get_similarity(word.text, pron)

        return score

    def launch_engine(self, sentence_doc: Doc) -> Engine:
        return self.engine_type(doc=sentence_doc)


functions_list = [
    Bridge(noun_list=["答案", "解", "数学"], verb_list=["求解", "计算", "等于", "加", "减", "乘"], pron_list=[],
           engine_type=MathematicsSolverEngine),  # Mathematics Solver
    Bridge(noun_list=["信息", "百科", "身份", "定义", "细节", "谁"], verb_list=["搜索", "告诉", "了解"], pron_list=["什么", "谁"],
           engine_type=WikiEngine),  # Wikipedia
    Bridge(noun_list=["天气", "雨", "雪", "风", "晴天", "明天", "后天"], verb_list=["下雨", "下雪", "晴", "打雷", "预测", "预知"], pron_list=[],
           engine_type=WeatherEngine)  # Weather
]
