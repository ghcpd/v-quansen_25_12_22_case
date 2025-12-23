import pytest

from src.api_client import fetch_user_profile, load_sample_response, normalize_profile


def test_load_sample_response_has_expected_keys():
    payload = load_sample_response()
    assert {"name", "email", "interests", "addresses"}.issubset(payload)


def test_normalize_profile_trims_and_lowercases():
    raw = {"name": " Ada ", "email": "Ada@EXAMPLE.com", "interests": [" math "]}
    normalized = normalize_profile(raw)
    assert normalized["name"] == "Ada"
    assert normalized["email"] == "ada@example.com"
    assert normalized["interests"] == ["math"]


def test_normalize_profile_filters_empty_interests():
    raw = {"name": "Test", "email": "t@example.com", "interests": ["dev", "", None]}
    normalized = normalize_profile(raw)
    assert normalized["interests"] == ["dev"]


def test_fetch_user_profile_only_supports_sample():
    with pytest.raises(ValueError):
        fetch_user_profile(source="other")
