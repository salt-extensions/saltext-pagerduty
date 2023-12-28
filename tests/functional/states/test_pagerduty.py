import pytest

pytestmark = [
    pytest.mark.requires_salt_states("pagerduty.exampled"),
]


@pytest.fixture
def pagerduty(states):
    return states.pagerduty


def test_replace_this_this_with_something_meaningful(pagerduty):
    echo_str = "Echoed!"
    ret = pagerduty.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
