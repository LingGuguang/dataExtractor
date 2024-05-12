# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from langchain.llms.base import LLM
from typing import (
    Optional,
    Any,
    List
)
from transformers import BitsAndBytesConfig
from langchain.callbacks.manager import CallbackManagerForLLMRun
import torch

class QwenLLMChat(LLM):
    tokenizer : AutoTokenizer = None
    model : AutoModelForCausalLM = None
    
    def __init__(self, model_path: str):
        super().__init__()
        nf4_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, 
                                                          trust_remote_code=True, 
                                                          device_map="cuda",
                                                          quantization_config=nf4_config)
        self.model.generation_config = GenerationConfig.from_pretrained(model_path)
        self.model = self.model.eval()

    def _call(self, prompt : str, stop: Optional[List[str]] = None,
                run_manager: Optional[CallbackManagerForLLMRun] = None,
                **kwargs: Any):

        messages = [{"role": "user", "content": prompt}]
        input_ids = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        model_inputs = self.tokenizer([input_ids], return_tensors="pt").to('cuda')
        generated_ids = self.model.generate(model_inputs.input_ids, max_new_tokens=512)
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return response
    
    @property
    def _llm_type(self) -> str:
        return "qwen1.5_LLM"

class baichuan2LLM(LLM):
    tokenizer : AutoTokenizer = None
    model : AutoModelForCausalLM = None

    def __init__(self, model_path : str):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, 
                                                       trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, 
                                                          trust_remote_code=True, 
                                                          torch_dtype=torch.bfloat16, 
                                                          device_map="auto")
        self.model.generation_config = GenerationConfig.from_pretrained(model_path)
        self.model = self.model.eval()

    def _call(self, prompt:str, stream:bool=False,
                stop: Optional[List[str]] = None,
                run_manager: Optional[CallbackManagerForLLMRun] = None,
                **kwargs: Any):
        messages = [
            {"role": "user", "content": prompt}
        ]
         # 重写调用函数
        response= self.model.chat(self.tokenizer, messages)
        print("response_from_call:",response)
        return response
    
    @property
    def _llm_type(self) -> str:
        return "baichuan2_LLM"