from src.pyinstrumentor.core import instrument
from prometheus_client import REGISTRY

def test_sync_function_metrics():
    calls = []

    @instrument
    def hello(name):
        calls.append(name)
        return f"Hello, {name}"

    result = hello("World")
    assert result == "Hello, World"
    assert len(calls) == 1

    metric = REGISTRY.get_sample_value("func_calls_total", {"function_name": "test_instrumentation.hello"})
    assert metric == 1.0