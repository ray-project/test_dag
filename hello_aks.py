# File name: serve_deployment.py
from starlette.requests import Request

import ray
from ray import serve
from ray.serve.deployment_graph import RayServeDAGHandle

from transformers import pipeline


@serve.deployment(ray_actor_options={"num_cpus": 0.2})
class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation

    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        # print(f"Received input: {english_text}")
        translation = self.translate(english_text)
        # print(f"Translated output: {translation}")
        return translation

@serve.deployment(ray_actor_options={"num_cpus": 0.1})
class BasicDriver:
    def __init__(self, dag: RayServeDAGHandle):
        self.dag = dag

    async def __call__(self, http_request: Request):
        object_ref = await self.dag.remote(http_request)
        # print(f"Received object reference: {object_ref}")
        result = await object_ref
        # print(f"Received result: {result}")
        return result

translator_app = Translator.bind()
# translation = translator_app.translate.bind()
DagNode = BasicDriver.bind(translator_app)