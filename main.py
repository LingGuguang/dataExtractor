"""
    利用大模型提取数据中的有效训练数据。
"""
from template_utils import TemplateExtractor
from LLMs import QwenLLMChat
from utils.basic import read_json

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate


datasets = read_json("test.json")


for data in datasets:
    id = data['id']
    context = data['input']
    answer = data['options'][data['gold_index']]
    


extractor = TemplateExtractor()



    




