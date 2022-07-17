import pytest


# https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option
def pytest_addoption(parser):
    parser.addoption( "--run-plotting", action="store_true", default=False, help="run plotting tests")


def pytest_configure(config):
    config.addinivalue_line("markers", "plotting: mark test as a plotting test")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-plotting"):
        # --run-plotting-tests given in cli: do not skip marked tests
        return
    skip_plotting = pytest.mark.skip(reason="need --run-plotting option to run")
    for item in items:
        if "plotting" in item.keywords:
            item.add_marker(skip_plotting)
