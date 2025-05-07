# status_dashboard module

def run(_: str = None) -> list:
    """
    Return a dashboard-style summary of known modules.
    """
    return [
        {"module": "prompt_parser", "version": "0.1.0", "refinement": 4, "status": "active"},
        {"module": "code_generator", "version": "0.1.0", "refinement": 4, "status": "active"},
        {"module": "self_improver", "version": "0.1.0", "refinement": 3, "status": "active"},
        {"module": "core_orchestrator", "version": "0.1.0", "refinement": 3, "status": "active"},
        {"module": "core_test_runner", "version": "0.1.0", "refinement": 5, "status": "active"},
        {"module": "string_utils", "version": "0.1.0", "refinement": 2, "status": "active"},
        {"module": "reverse_string", "version": "0.1.0", "refinement": 5, "status": "planned"},
        {"module": "status_dashboard", "version": "0.1.0", "refinement": 4, "status": "active"}
    ]