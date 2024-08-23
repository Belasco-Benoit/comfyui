import json
import random

class JSONPromptLoader:
    def __init__(self):
        self.prompts = []

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_file": ("STRING", {"default": "prompts.json"}),
                "mode": (["sequential", "random"], {"default": "sequential"}),
                "external_index": ("INT", {"default": 0, "min": 0, "max": 99999})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_prompt"
    CATEGORY = "prompt"

    def load_prompt(self, json_file, mode, external_index):
        if not self.prompts:
            with open(json_file, 'r') as f:
                self.prompts = json.load(f)
        
        if mode == "sequential":
            prompt = self.prompts[external_index % len(self.prompts)]
        else:  # random
            random.seed(external_index)  # Use external_index as seed for reproducibility
            prompt = random.choice(self.prompts)
        
        return (prompt,)


class Counter:
    def __init__(self):
        self.count = 0

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "increment": ("INT", {"default": 1, "min": 1, "max": 999})
            }
        }
    
    RETURN_TYPES = ("INT",)
    FUNCTION = "count"
    CATEGORY = "utils"

    def count(self, increment):
        self.count += increment
        return (self.count,)

NODE_CLASS_MAPPINGS = {
    "JSONPromptLoader": JSONPromptLoader,
    "Counter": Counter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONPromptLoader": "JSON Prompt Loader",
    "Counter": "Counter"
}