def clean_text(text: str) -> str:
    """Заменяет \\t и \\n на пробелы, лишние пробелы обрезает."""
    if not text:
        return ""
    # Убираю табы и переводы строк, заменяем на пробел
    cleaned = text.replace("\t", " ").replace("\n", " ")
    # Разбиваю на слова и соединяем одним пробелом, чтобы убрать лишние
    return " ".join(cleaned.split())
