def is_empty(value):
    """
    Sprawdza, czy wartość jest pusta.

    Args:
        value (any): dowolna wartość do sprawdzenia (str, None, liczby itp.)

    Returns:
        bool: True jeśli wartość jest None lub (pustym/whitespace) stringiem, False w przeciwnym razie.
    """
    return value is None or str(value).strip() == ""
