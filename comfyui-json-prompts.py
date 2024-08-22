import json
import random
from server import PromptServer

class JSONPromptLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_file": ("STRING", {"default": "prompts.json"}),
                "mode": (["sequential", "random"], {"default": "sequential"})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_prompt"
    CATEGORY = "prompt"

    def __init__(self):
        self.prompts = []
        self.current_index = 0

    def load_prompt(self, json_file, mode):
        if not self.prompts:
            with open(json_file, 'r') as f:
                self.prompts = json.load(f)
        
        if mode == "sequential":
            prompt = self.prompts[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.prompts)
        else:  # random
            prompt = random.choice(self.prompts)
        
        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "JSONPromptLoader": JSONPromptLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONPromptLoader": "JSON Prompt Loader"
}