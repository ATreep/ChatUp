import sys

import spacy
import lexicon
import TTS
from VioceRecognition import recognition_engine

nlp = spacy.load("zh_core_web_trf")

while True:
    sentence = ""

    cmd = input("\nChatUp *** 输入 “T” 以键入文字；输入 “V” 以识别语音。\n")
    if cmd.strip().upper() == "T":
        sentence = input("请输入: ")
    elif cmd.strip().upper() == "V":
        sentence = recognition_engine.baidu_speech_to_text()
        print(sentence)
    else:
        sys.exit(0)

    doc = nlp(sentence)

    matching_rates = []

    for func_bridge in lexicon.functions_list:
        matching_rates.append(func_bridge.match(doc))

    numeric_matching_rates = enumerate(matching_rates)
    sorted_numeric_matching_rates = sorted(numeric_matching_rates, key=lambda x: x[1], reverse=True)

    engine = lexicon.functions_list[sorted_numeric_matching_rates[0][0]].launch_engine(doc)

    print("\nChatUp:")

    print(engine.output())

    TTS.play_sound(engine.output())
