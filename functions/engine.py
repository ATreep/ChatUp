from spacy.tokens import Doc


class Engine:
    output_text = ""
    purpose = ""

    def __init__(self, doc: Doc):
        self.doc = doc

    def output(self) -> str:
        return self.output_text + f"\n如果你的目的不是 {self.purpose}，请更加详细准确地描述你的问题。"
