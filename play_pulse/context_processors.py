import settings


def debug() -> dict[str, bool]:
    """Возвращает словарь с текущим значением настройки DEBUG.

    :return Словарь с ключом DEBUG и его текущим значением из настроек Django.
    """
    return {'DEBUG': settings.DEBUG}
