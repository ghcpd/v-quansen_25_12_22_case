import pytest

from src.api_client import load_sample_response
from src.data_processor import summarize_user_profile


def test_summarize_user_profile_returns_primary_interest():
    raw = {
        "name": "Ada",
        "email": "ada@example.com",
        "interests": ["math", "computing"],
        "addresses": [{"city": "London"}],
    }
    summary = summarize_user_profile(raw)
    assert summary["primary_interest"] == "math"


def test_summarize_user_profile_handles_missing_city():
    raw = {"name": "Ada", "email": "ada@example.com", "interests": ["math"], "addresses": []}
    summary = summarize_user_profile(raw)
    assert summary["city"] is None


def test_integration_with_sample_data():
    raw = load_sample_response()
    summary = summarize_user_profile(raw)
    assert summary == {
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "primary_interest": "math",
        "city": "London",
    }


def test_graceful_degradation_on_missing_email_and_interests():
    raw = {"name": "  Mystery User  ", "email": None, "interests": [], "addresses": []}
    summary = summarize_user_profile(raw)
    assert summary == {
        "name": "Mystery User",
        "email": "unknown@example.com",
        "primary_interest": None,
        "city": None,
    }


def test_primary_interest_missing_interests_list_index_error_scenario():
    """Explicitly cover the list index out of bounds case when interests are empty."""
    raw = {"name": "Edge", "email": "edge@example.com", "interests": [], "addresses": []}
    summary = summarize_user_profile(raw)
    assert summary == {
        "name": "Edge",
        "email": "edge@example.com",
        "primary_interest": None,
        "city": None,
    }
