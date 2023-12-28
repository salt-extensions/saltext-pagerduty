import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("pagerduty.example_function"),
]


@pytest.fixture
def pagerduty(modules):
    return modules.pagerduty


def test_replace_this_this_with_something_meaningful(pagerduty):
    echo_str = "Echoed!"
    res = pagerduty.example_function(echo_str)
    assert res == echo_str
