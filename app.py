from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
from huggingface_hub import snapshot_download
import os

class InferlessPythonModel:
    def initialize(self):
        print("Hello World 13")

    def infer(self, inputs):
        prompts = inputs["prompt"]
        print(prompts)
        if len(prompts) > 1:
            prompt = prompts[0]
        else
            prompt = prompts
        image = self.pipe(prompt).images[0]        
        return { "generated_image_base64" : "sample" }
        
    def finalize(self):
        self.pipe = None
