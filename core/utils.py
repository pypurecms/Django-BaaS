from django.conf import settings


def __get_model(name):
    return settings.MODEL_DICT.get(name, {})


def get_url_name(name):
    return __get_model(name).get('plural', name).lower()


def get_enabled(name):
    return __get_model(name).get('enable', False)


def get_model_name(name):
    return __get_model(name).get('name', name).capitalize()


def get_plural_name(name):
    return __get_model(name).get('plural', name).capitalize()
