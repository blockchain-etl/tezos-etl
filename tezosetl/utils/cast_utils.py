def safe_int(val, default=None):
    if val is None:
        return val
    try:
        return int(val)
    except (ValueError, TypeError):
        return default
