def pytest_sessionfinish(session, exitstatus):
    # For Loop for printing branches
    from rich._log_render import BRANCH_COVERAGE

    print("\n BRANCH COVERAGE FOR DIY:")
    for i in (BRANCH_COVERAGE):
        print(f"{i}: {BRANCH_COVERAGE[i]}")