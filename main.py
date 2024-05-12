"""
    利用大模型提取数据中的有效训练数据。
"""
from utils.utilsForTemplate import TemplateExtractor
from LLMs import QwenLLMChat
from utils.utils import read_json

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

from dataExtractor import fewShotExtractor

datasets = read_json("test.json")[:2]

extractor = fewShotExtractor()
QAlist = []
for data in datasets:
    ids = data['ids']
    input = data['input']
    QAtemp = extractor.extract(input)
    QAlist.extend(QAtemp)
    print(type(QAtemp), QAtemp)





    




