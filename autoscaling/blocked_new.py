import ray
from ray import serve

@serve.deployment
class Blocked:
    def __call__(self):
        signal = serve.get_deployment_handle("SignalDeployment", app_name="signal")
        ref = signal.wait.remote()
        ref.result()
        return "hello"

app = Blocked.bind()
