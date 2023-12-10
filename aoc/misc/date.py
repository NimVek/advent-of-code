import datetime
import zoneinfo

import logging


__log__ = logging.getLogger(__name__)


now = datetime.datetime.now(tz=zoneinfo.ZoneInfo("EST"))
today = now.date()
