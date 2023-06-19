from spacy.tokens import Doc
import utils
from functions.engine import Engine

math_symbols = [
    ("加", "+"),
    ("加上", "+"),
    ("减", "-"),
    ("减去", "-"),
    ("乘", "*"),
    ("乘上", "*"),
    ("乘以", "*"),
    ("除以", "/"),
    ("除去", "/"),
    ("除", "/")
]


class MathematicsSolverEngine(Engine):
    purpose = "解决数学问题"

    def __init__(self, doc: Doc):
        super().__init__(doc)

        math_expression = ""
        is_started_expression = False
        is_not_in_expression = True
        for word_doc in doc:
            if is_started_expression and is_not_in_expression:
                break
            if word_doc.text in ("+", "-", "*"):
                is_started_expression = True
                is_not_in_expression = False
                math_expression += word_doc.text
            elif word_doc.pos_ == "NUM":
                try:
                    math_expression += utils.convert_chinese_numeral(word_doc.text)
                    is_started_expression = True
                    is_not_in_expression = False
                except ValueError:
                    pass
            elif word_doc.pos_ == "VERB":
                for t in math_symbols:
                    if word_doc.text == t[0] or utils.get_similarity(word_doc.text, t[0]) >= 0.8:
                        math_expression += t[1]
                        is_started_expression = True
                        is_not_in_expression = False
                        break
            else:
                is_not_in_expression = True

            self.expression = math_expression
            self.cal_result = 0.0
            self.cal_successfully = False
            try:
                self.cal_result = utils.calculate_math_expression(self.expression)
                self.cal_successfully = True
            except SyntaxError:
                pass

        if self.cal_successfully:
            self.output_text += f"公式 {self.expression} 的计算结果为 {self.cal_result}。"
        else:
            self.output_text += f"抱歉，我无法计算 {self.expression}。"
