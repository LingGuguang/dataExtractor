from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

import os, sys
from templateSet import FEW_SHOT_TEMPLATE, fewshotSchema



def fewshotExtractorTemplate():
    output_parser = fewshotSchema()
    format_instructions = output_parser.get_format_instructions()
    prompt = ChatPromptTemplate.from_template(template=FEW_SHOT_TEMPLATE)
    message = prompt.partial(format_instructions=format_instructions)
    return message, output_parser

if __name__ == "__main__":
    print(fewshotExtractorTemplate())