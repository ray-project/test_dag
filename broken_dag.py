from ray import serve

class CustomException(Exception):

    def __init__(self, *args):
        import matplotlib
        self.version = matplotlib.__version__

raise CustomException("This is a custom exception!")

@serve.deployment
def f(*args):
    return "Hi there!"

app = f.bind()
