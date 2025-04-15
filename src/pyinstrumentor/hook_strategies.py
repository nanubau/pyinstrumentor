from prometheus_client import Counter

exception_counter = Counter(
    "exceptions_total",
    "Total number of exceptions raised, by type and function",
    ["function_name", "exception_type"]
)

def track_exceptions_by_type(args, kwargs, result=None, exception=None, function_name=None):
    if exception:
        ex_type = type(exception).__name__
        exception_counter.labels(function_name=function_name, exception_type=ex_type).inc()
