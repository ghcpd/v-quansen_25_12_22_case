"""
Transform normalized profile data into a compact summary. The implementation
intentionally contains a couple of sharp edges to highlight defensive coding
practices when working with third-party data.
"""
from __future__ import annotations

from typing import Any, Dict, Optional

from src.api_client import normalize_profile


def summarize_user_profile(raw_profile: Dict[str, Any]) -> Dict[str, Optional[str]]:
    """Summarize a profile into a small, display-friendly shape."""
    profile = normalize_profile(raw_profile)

    # Handle empty interests list by returning None.
    interests = profile.get("interests") or []
    primary_interest = interests[0] if interests else None

    addresses = profile.get("addresses") or []
    city = addresses[0].get("city") if addresses else None

    return {
        "name": profile.get("name"),
        "email": profile.get("email"),
        "primary_interest": primary_interest,
        "city": city,
    }
