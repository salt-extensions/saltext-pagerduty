"""
:codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from saltext.pagerduty.states import pagerduty


@pytest.fixture
def configure_loader_modules():
    return {pagerduty: {}}


def test_create_event():
    """
    Test to create an event on the PagerDuty service.
    """
    name = "This is a server warning message"
    details = "This is a much more detailed message"
    service_key = "9abcd123456789efabcde362783cdbaf"
    profile = "my-pagerduty-account"

    ret = {"name": name, "result": None, "comment": "", "changes": {}}

    with patch.dict(pagerduty.__opts__, {"test": True}):
        comt = f"Need to create event: {name}"
        ret.update({"comment": comt})
        assert pagerduty.create_event(name, details, service_key, profile) == ret

    with patch.dict(pagerduty.__opts__, {"test": False}):
        mock_t = MagicMock(return_value=True)
        with patch.dict(pagerduty.__salt__, {"pagerduty.create_event": mock_t}):
            comt = f"Created event: {name}"
            ret.update({"comment": comt, "result": True})
            assert pagerduty.create_event(name, details, service_key, profile) == ret
