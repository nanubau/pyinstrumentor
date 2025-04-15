import pytest
from prometheus_client import REGISTRY, Counter
from pyinstrumentor.core import instrument
from pyinstrumentor.hooks import register_hook, register_global_hook
from pyinstrumentor.hook_strategies import track_exceptions_by_type

# --- Basic sync and async functions ---
@instrument
def add(a, b):
    return a + b

@instrument
def return_none():
    return None

@instrument
def raise_value_error():
    raise ValueError("Something went wrong")

import asyncio

@instrument
async def async_add(a, b):
    return a + b

# --- Hook Test State ---
custom_counter = Counter("custom_hook_calls", "Number of times custom hook was called", ["function_name"])
global_none_counter = Counter("global_none_counter", "Count None returns", ["function_name"])

# --- Hook Definitions ---
def custom_hook(args, kwargs, result=None, exception=None, function_name=None):
    custom_counter.labels(function_name=function_name).inc()

def count_none_return(args, kwargs, result=None, exception=None, function_name=None):
    if result is None:
        global_none_counter.labels(function_name=function_name).inc()

# --- Register Hooks ---
register_hook("test_pyinstrumentor.add", custom_hook)
register_global_hook(count_none_return)
register_global_hook(track_exceptions_by_type)

# --- TEST CASES ---

def test_sync_add():
    assert add(2, 3) == 5
    metric = REGISTRY.get_sample_value("func_calls_total", {"function_name": "test_pyinstrumentor.add"})
    assert metric == 1.0

def test_return_none():
    assert return_none() is None
    metric = REGISTRY.get_sample_value("global_none_counter", {"function_name": "test_pyinstrumentor.return_none"})
    assert metric == 1.0

def test_exception_tracking():
    with pytest.raises(ValueError):
        raise_value_error()
    metric = REGISTRY.get_sample_value("exceptions_total", {
        "function_name": "test_pyinstrumentor.raise_value_error",
        "exception_type": "ValueError"
    })
    assert metric == 1.0

@pytest.mark.asyncio
async def test_async_function():
    result = await async_add(5, 7)
    assert result == 12
    metric = REGISTRY.get_sample_value("func_calls_total", {"function_name": "test_pyinstrumentor.async_add"})
    assert metric == 1.0
