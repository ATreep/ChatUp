# Introduction
ChatUp, a simple Chinese voice assistant based on NLP.
## Functions
- Resolve simple mathematical problems.
        
        “请帮我解决三十九加上二十七。”
        “五十七乘以二十九等于多少？”

- Search concepts in Baidu Wikipedia.

        “请告诉我霍金是谁？”
        “我想了解坦克的有关信息。”
        “什么是电脑？”

- Weather forecast.

        “青岛市明天会下雨吗？”
        “上海未来的天气怎么样？”
        “请告诉我昆明后天有雪吗？”

## Limitation
- The low degree of accuracy in language understanding.
- Few functions.
- Do not support multiple languages.

## Developing Period of Current Version
- Version: 0.0.1
- Period: 3 days.

# Guide of Setting Environment
## System and Interpreter Requirement
- Windows
- Python 3.X
## About Runtime.7z
I packed the SpaCy model and NLTK extensions in one 7z file. Please unpack it before following configurations in the next part.

Or you could download and install them manually.

- 从**百度网盘**下载 Runtime.7z
```
链接：https://pan.baidu.com/s/1t6yNtLssTmKF3oqvstLiwg?pwd=ijue 
提取码：ijue
```
- Download Runtime.7z from **OneDrive**
```
https://1drv.ms/u/s!AouY4vmTrbY6g6EPYDaDpKJxSr68qw?e=fSVB3U
```
## Configurate Modules
1. Install modules by :
```batch
pip install -r requirements.txt
```
2. Install SpaCy model of Chinese by:
```batch
cd Runtime\spacy
pip install zh_core_web_trf-3.5.0.tar.gz
```
3. Copy folder **Runtime\nltk_data** to **C:\Users\\&lt;username>\AppData\Roaming\nltk_data**
4. Get APP_ID, API_KEY and SECRET_KEY from [Baidu AI Cloud](https://cloud.baidu.com/). Fill in **baidu_api.py** with your ID and Keys.