from ray import serve
import numpy as np

class CustomException(Exception):

    def __init__(self, *args):
        self.zeros = np.zeros(5)

raise CustomException("This is a custom exception!")

@serve.deployment
def f(*args):
    return "Hi there!"

app = f.bind()
