from typing import List, Dict
from utils.utilsForTemplate import fewshotExtractorTemplate
from langchain.prompts import PromptTemplate
from LLMs import QwenLLMChat
import os, sys
from langchain.llms.base import LLM
from langchain.chains.conversation.base import LLMChain



class fewShotExtractor:
    model: LLM = None
    output_key: str = "output"

    def __init__(self, 
                 llm: LLM,
                 ):
        prompt, output_parser = fewshotExtractorTemplate()

        self.llm_chain = LLMChain(
            llm=llm, 
            prompt=prompt,
            return_final_only=True,
            verbose=True,
            output_key=self.output_key,# 设置输出内容的占位符，这使得该输出可以直接被后续链中的template直接使用。
            # input_key="input", # 设置conversation的新输入的占位符
            output_parser=output_parser,
        )

    def set_output_key(self, output_key):
        self.output_key = output_key

    def extract(self, input: str) -> List[Dict]:
        return self.llm_chain.invoke(input=input, return_only_outputs=True)[self.output_key]











