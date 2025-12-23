# Runtime Error 1222 – Defensive Programming Lab

Minimal Python project (Windows-friendly) that demonstrates two classic runtime errors when integrating with third-party data: null-pointer style `AttributeError` and list index out of range. The suite includes 7 passing and 1 intentionally failing test to make the problems reproducible.

## Project Layout

```
src/
  api_client.py      # mock third-party payload + normalization step (null-pointer bug lives here)
  data_processor.py  # composes normalized data (index-out-of-range bug lives here)
tests/
  test_api_client.py
  test_data_processor.py
data/
  sample_response.json
README.md
KNOWN_ISSUE.md
requirements.txt
```

## Quickstart

```bash
python -m pip install -r requirements.txt
pytest
```

Expected: 7 tests pass, 2 fail (the failures are the learning targets).

## Reproduction Paths

1. **Unit tests**: Run `pytest` to hit both the null-pointer and list index bugs via `test_graceful_degradation_on_missing_email_and_interests` and `test_primary_interest_missing_interests_list_index_error_scenario`.
2. **Manual call**: In a Python shell run:
   ```python
   from src.data_processor import summarize_user_profile
   summarize_user_profile({"name": " Mystery ", "email": None, "interests": [], "addresses": []})
   ```
   This raises `AttributeError` and, once fixed, would raise `IndexError` because of the empty interests list.
3. **Sample data**: The happy-path sample in `data/sample_response.json` keeps most tests green so you can focus on the edge case.

## Learning Goals

- Defensive checks around nullable data from external systems.
- Guarding list access to avoid out-of-bounds errors.
- Using tests to document and reproduce integration edge cases.
