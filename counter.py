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
    CATEGORY = "prompt"

    def count(self, increment):
        self.count += increment
        return (self.count,)

NODE_CLASS_MAPPINGS["Counter"] = Counter