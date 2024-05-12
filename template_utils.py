from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from utils.template import (
    EXTRACTOR_TEMPLATE
)


class TemplateExtractor:
    template = PromptTemplate(EXTRACTOR_TEMPLATE)
 
    def get_extractor(self, text):
        
        return self.template.partial(text)
    
    def __getitem__(self):
        return self.template