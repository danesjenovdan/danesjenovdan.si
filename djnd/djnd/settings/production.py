from .base import *

DEBUG = bool(os.getenv("DJANGO_DEBUG", False))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "<TODO>")

ALLOWED_HOSTS = ["staging.danesjenovdan.si"]
CSRF_TRUSTED_ORIGINS = ["https://staging.danesjenovdan.si"]

WAGTAILADMIN_BASE_URL = "https://staging.danesjenovdan.si"

STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, "static"))
STATIC_URL = os.getenv("DJANGO_STATIC_URL_BASE", "/static/")

if os.getenv("DJANGO_ENABLE_S3", False):
    STORAGES["default"] = {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    }
    AWS_ACCESS_KEY_ID = os.getenv("DJANGO_AWS_ACCESS_KEY_ID", "<TODO>")
    AWS_SECRET_ACCESS_KEY = os.getenv("DJANGO_AWS_SECRET_ACCESS_KEY", "<TODO>")
    AWS_STORAGE_BUCKET_NAME = os.getenv("DJANGO_AWS_STORAGE_BUCKET_NAME", "djnd")
    AWS_DEFAULT_ACL = "public-read"
    AWS_QUERYSTRING_AUTH = False
    AWS_LOCATION = os.getenv("DJANGO_AWS_LOCATION", "danesjenovdan-staging")
    AWS_S3_REGION_NAME = os.getenv("DJANGO_AWS_REGION_NAME", "fr-par")
    AWS_S3_ENDPOINT_URL = os.getenv(
        "DJANGO_AWS_S3_ENDPOINT_URL", "https://s3.fr-par.scw.cloud"
    )
    AWS_S3_SIGNATURE_VERSION = os.getenv("DJANGO_AWS_S3_SIGNATURE_VERSION", "s3v4")
    AWS_S3_FILE_OVERWRITE = False

if sentry_url := os.getenv("DJANGO_SENTRY_URL", False):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        sentry_url,
        integrations=[DjangoIntegration()],
        send_default_pii=True,
        max_request_body_size="always",
        traces_sample_rate=0,
        send_client_reports=False,
        auto_session_tracking=False,
    )
