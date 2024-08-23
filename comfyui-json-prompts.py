import json
import random
import logging
logging.basicConfig(level=logging.INFO)


class JSONPromptLoader:
    def __init__(self):
        self.prompts = []
        logging.info("JSONPromptLoader initialized")
        
    @classmethod
    def INPUT_TYPES(s):
        logging.info("JSONPromptLoader INPUT_TYPES called")
        return {
            "required": {
                "json_file": ("STRING", {"default": "prompts.json"}),
                "mode": (["sequential", "random"], {"default": "sequential"}),
                "external_index": ("INT", {"forceInput": True, "default": 0, "min": 0, "max": 99999})
                
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


class CustomCounter:
    def __init__(self):
        self.count = 0
        logging.info("Counter initialized with count: %d", self.count)

    @classmethod
    def INPUT_TYPES(s):
        logging.info("Counter INPUT_TYPES called")
        return {
            "required": {
                "increment": ("INT", {"default": 1, "min": 1, "max": 999})
            }
        }
    
    RETURN_TYPES = ("INT",)
    FUNCTION = "increment_count"
    CATEGORY = "utils"

    def increment_count(self, increment):
        logging.info("Counter.count called with increment: %d", increment)
        self.count += increment
        logging.info("New count: %d", self.count)
        return (self.count,)

NODE_CLASS_MAPPINGS = {
    "JSONPromptLoader": JSONPromptLoader,
    "Counter": CustomCounter
}

logging.info("NODE_CLASS_MAPPINGS: %s", NODE_CLASS_MAPPINGS)

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONPromptLoader": "JSON Prompt Loader",
    "Counter": "Counter"
}