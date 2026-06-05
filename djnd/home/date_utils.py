from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from django.conf import settings


def to_datetime(in_date):
    if not in_date:
        return None
    if isinstance(in_date, datetime):
        return in_date
    if isinstance(in_date, date):
        return datetime.combine(
            in_date,
            time.min,
            tzinfo=ZoneInfo(settings.TIME_ZONE),
        )
    return None
