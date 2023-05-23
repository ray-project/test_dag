from ray import serve

class CustomException(Exception):
    pass

raise CustomException("This is a custom exception!")

@serve.deployment
def f(*args):
    return "Hi there!"

app = f.bind()
