from ray import serve
import yaml

class CustomException(Exception):

    def __init__(self, *args):
        yaml.safe_load("[]")

raise CustomException("This is a custom exception!")

@serve.deployment
def f(*args):
    return "Hi there!"

app = f.bind()
