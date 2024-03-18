def assert_calls(object, methods: list[str], params: list, results: list):
    for method, param, result in zip(methods, params, results):
        method_def = getattr(object, method)
        assert result == method_def(*param)
