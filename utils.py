from nltk.corpus import wordnet as wn
import cn2an
import numexpr as ne


def get_similarity(word1: str, word2: str) -> float:
    word1_syn = wn.synsets(word1, lang="cmn")
    word2_syn = wn.synsets(word2, lang="cmn")
    return max((s1.path_similarity(s2) for s1 in word1_syn for s2 in word2_syn), default=0)


def convert_chinese_numeral(numeral: str) -> str:
    return str(cn2an.cn2an(numeral, "smart"))


def calculate_math_expression(exp: str) -> float:
    return ne.evaluate(exp).item()
