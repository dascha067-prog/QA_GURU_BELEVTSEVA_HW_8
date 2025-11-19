from enum import StrEnum


class Status(StrEnum):
    """Статусы письма в процессе подготовки и отправки."""

    DRAFT = "draft"  # Черновик, письмо еще не готово
    READY = "ready"  # Готово к отправке
    SENT = "sent"  # Успешно отправлено
    FAILED = "failed"  # Ошибка при отправке
    INVALID = "invalid"  # Невалидное (некорректное) письмо
