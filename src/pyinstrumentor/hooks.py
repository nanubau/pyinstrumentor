_user_hooks = {}

def register_hook(function_name, hook_fn):
    _user_hooks[function_name] = hook_fn

def apply_user_hooks(function_name, args, kwargs):
    if function_name in _user_hooks:
        _user_hooks[function_name](args, kwargs)