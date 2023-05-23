from ray import serve

class CustomException(Exception):

    def __init__(self, *args):
        import numpy as np
        self.zeros = np.zeros(5)

raise CustomException("This is a custom exception!")

@serve.deployment
def f(*args):
    return "Hi there!"

app = f.bind()
