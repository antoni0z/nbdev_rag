# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_llm.ipynb.

# %% auto 0
__all__ = ['LLM', 'PromptTemplate']

# %% ../nbs/04_llm.ipynb 2
import torch

# %% ../nbs/04_llm.ipynb 3
class LLM:
    """Class for interacting and Loading llms, tested with hugging face ones and it works correctly"""
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if hasattr(self.model, "is_quantized") and not self.model.is_quantized:
            self.model.to(self.device)

    def __call__(self, prompt, max_length=100):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        output_ids = self.model.generate(input_ids=input_ids, max_length=max_length, eos_token_id=self.tokenizer.eos_token_id, pad_token_id=self.tokenizer.pad_token_id)
        response = self.tokenizer.decode(output_ids[0], skip_special_tokens=True).strip(prompt)
        return response

# %% ../nbs/04_llm.ipynb 4
class PromptTemplate:
    """Class for prompt templating and adding intructions for an LLM"""
    def __init__(self, template = 'A user provided this instructions'):
        self.template = template

    def __call__(self, input_text):
        self.prompt = f"{self.template}: {input_text} Output:"
        return self.prompt
