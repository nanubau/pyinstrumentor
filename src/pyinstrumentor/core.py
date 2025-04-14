import functools
import inspect
from .metrics import FUNC_CALL_COUNTER, FUNC_EXEC_TIME
from .hooks import apply_user_hooks

def instrument(func):
    name = f"{func.__module__}.{func.__qualname__}"
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            FUNC_CALL_COUNTER.labels(function_name=name).inc()
            with FUNC_EXEC_TIME.labels(function_name=name).time():
                apply_user_hooks(name, args, kwargs)
                return await func(*args, **kwargs)
        return async_wrapper
    else:
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            FUNC_CALL_COUNTER.labels(function_name=name).inc()
            with FUNC_EXEC_TIME.labels(function_name=name).time():
                apply_user_hooks(name, args, kwargs)
                return func(*args, **kwargs)
        return sync_wrapper