def word_count(text):
    """
    Zwraca liczbę słów w podanym tekście.

    Args:
        text (str): tekst do policzenia słów

    Returns:
        int: liczba słów w tekście (0 jeśli pusty string)
    """
    return len(text.split())
