_user_hooks = {}
_global_hooks = []

def register_hook(function_name, hook_fn):
    _user_hooks[function_name] = hook_fn

def register_global_hook(hook_fn):
    _global_hooks.append(hook_fn)

def apply_user_hooks(function_name, args, kwargs, result=None, exception=None):
    # Per-function hook
    if function_name in _user_hooks:
        try:
            _user_hooks[function_name](args, kwargs, result=result, exception=exception, function_name=function_name)
        except Exception as e:
            print(f"[pyinstrumentor] Error in hook for {function_name}: {e}")
    
    # Global hooks
    for hook in _global_hooks:
        try:
            hook(args, kwargs, result=result, exception=exception, function_name=function_name)
        except Exception as e:
            print(f"[pyinstrumentor] Error in global hook: {e}")
