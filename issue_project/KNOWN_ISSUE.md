# Known Issues

1. **Null-like email handling (AttributeError)**
   - Location: `normalize_profile` in `src/api_client.py`
   - Trigger: `email` is `None`; calling `.lower()` throws `AttributeError`.
   - Expected: tolerate missing email and fall back to a placeholder.
2. **Empty interests list (IndexError)**
   - Location: `summarize_user_profile` in `src/data_processor.py`
   - Trigger: `interests` is empty; indexing `interests[0]` raises `IndexError`.
   - Expected: return `None` or a friendly message when interests are missing.
   - Repro: `tests/test_data_processor.py::test_primary_interest_missing_interests_list_index_error_scenario`

See `tests/test_data_processor.py::test_graceful_degradation_on_missing_email_and_interests` for a reproducible failing case that exercises both issues together.
