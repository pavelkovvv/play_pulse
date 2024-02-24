from django.conf import settings


def debug_context(request) -> dict[str, bool]:  # noqa: ARG001
    """Возвращает словарь с текущим значением настройки DEBUG.

    :return Словарь с ключом DEBUG и его текущим значением из настроек Django.
    """
    return {'DEBUG': settings.DEBUG}
