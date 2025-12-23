"""
Lightweight API client mock that simulates pulling user profile data from a
third-party service. The goal is to illustrate how missing fields can lead to
runtime issues when defensive checks are skipped.
"""
from __future__ import annotations

from pathlib import Path
import json
from typing import Any, Dict, List


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_response.json"


def load_sample_response(path: Path = DATA_PATH) -> Dict[str, Any]:
    """Load the bundled sample response from disk."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fetch_user_profile(source: str = "sample") -> Dict[str, Any]:
    """
    Pretend to fetch user profile data from a remote API. In this demo we only
    support the built-in sample but the signature mirrors an integration point
    for swapping in real HTTP calls.
    """
    if source != "sample":
        raise ValueError("Only the 'sample' source is supported in this demo")
    return load_sample_response()


def normalize_profile(raw_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize a raw profile payload. This intentionally omits some defensive
    checks to demonstrate common failure modes when third-party data is missing
    or incomplete.
    """
    name = (raw_profile.get("name") or "").strip()

    # BUG: lower() on None when email is missing -> classic null pointer error.
    email = raw_profile.get("email").lower()  # type: ignore[union-attr]

    # Remove falsy entries and trim whitespace.
    interests: List[str] = [interest.strip() for interest in raw_profile.get("interests", []) if interest]

    addresses = raw_profile.get("addresses") or []

    return {
        "name": name,
        "email": email,
        "interests": interests,
        "addresses": addresses,
    }
