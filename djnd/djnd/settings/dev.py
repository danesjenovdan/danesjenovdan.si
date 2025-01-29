from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y0p=ujxevu6)stsx!c(umnpz45#8@e)-xm-d@a(#22&jap(7!%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


def request_filter(record):
    if isinstance(record.args[0], str):
        if record.args[0] == "Not Found":
            return False
        if record.args[0].startswith("GET /media/"):
            return False
        if record.args[0].startswith("GET /static/"):
            return False
    return True


DEFAULT_LOGGING["filters"]["request_filter"] = {
    "()": "django.utils.log.CallbackFilter",
    "callback": request_filter,
}
DEFAULT_LOGGING["handlers"]["console"]["filters"] = ["request_filter"]
DEFAULT_LOGGING["handlers"]["django.server"]["filters"] = ["request_filter"]
