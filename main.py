"""
    利用大模型提取数据中的有效训练数据。
"""
from LLMs import QwenLLMChat
from utils.basicUtils import read_json

from dataExtractor import fewShotExtractor
import os, sys

datasets = read_json("test.json")[:2]
current_path = os.path.dirname(sys.path[0])
model_path = os.path.join(current_path, "LLModel/qwen1.5-14B-chat")
llm = QwenLLMChat(model_path)
extractor = fewShotExtractor(llm)
QAlist = []
for data in datasets:
    ids = data['ids']
    input = data['input']
    QAtemp = extractor.extract(input)
    QAlist.extend(QAtemp)
    print(type(QAtemp), QAtemp)





    




