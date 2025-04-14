from prometheus_client import Counter, Summary

FUNC_CALL_COUNTER = Counter("func_calls_total", "Function call count", ["function_name"])
FUNC_EXEC_TIME = Summary("func_exec_time_seconds", "Execution time", ["function_name"])