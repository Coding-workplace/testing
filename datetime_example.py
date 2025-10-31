from datetime import date, time, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# Creating date/time/datetime objects

# date
d = date(2025, 10, 31)

# time (hour, minute, second, microsecond)
t = time(14, 30, 5, 123456)

# naive datetime (no tz)
dt_naive = datetime(2025, 10, 31, 14, 30, 5, 123456)

# aware datetime (UTC)
dt_utc = datetime(2025, 10, 31, 14, 30, 5, tzinfo=timezone.utc)

# combine date + time
dt_combo = datetime.combine(d, t)


# Time stamp and epoch conversion

# current time as aware UTC
now_utc = datetime.now(timezone.utc)

# current timestamp
ts = now_utc.timestamp()

# from timestamp --> aware UTC datetime
dt_from_ts = datetime.fromtimestamp(ts, tz=timezone.utc)

# naive from timestamp (system local time)
dt_local_naive = datetime.fromtimestamp(ts)

# Formatting and Parsing
fmt = "%Y-%m-%d %H:%M:%S%z"
s = now_utc.strftime(fmt) 
s = "2025-10-31 14:30:05+00:00"
dt = datetime.fromisoformat(s)          # handles ISO 8601 well
dt2 = datetime.strptime("2025-10-31 14:30", "%Y-%m-%d %H:%M")


# Time deltas and arithmetic

now = datetime.now()
delta = timedelta(days=3, hours=4, minutes=30)

future = now + delta
past = now - timedelta(weeks=1)

# difference between datetimes -> timedelta
diff = future - now
seconds = diff.total_seconds()
 
 
 
# Core: tzinfo is abstract. For simple fixed offsets use datetime.timezone; for IANA zone rules use zoneinfo (Python 3.9+)
dt_ny = datetime(2025, 3, 9, 1, 30, tzinfo=ZoneInfo("America/New_York"))
dt_utc = dt_ny.astimezone(ZoneInfo("UTC"))


# Edge cases: DST transitions may produce ambiguous or non-existent local times. zoneinfo raises or marks ambiguity — handle with careful logic (e.g., prefer fold attribute).

# disambiguate repeated times in fall-back DST
dt1 = datetime(2025, 11, 2, 1, 30, tzinfo=ZoneInfo("America/New_York"))
dt1 = dt1.replace(fold=1)  # choose the second occurrence

## 6 — ISO 8601, RFC3339, and best storage format

# For interchange/store: use UTC ISO 8601:
dt.astimezone(timezone.utc).isoformat()  # e.g., "2025-10-31T14:30:05+00:00"
# For databases: store as TIMESTAMP WITH TIME ZONE (if DB supports) or store numeric epoch (int ms/seconds) + timezone metadata.

# Conversion to/from epoch ms:

millis = int(dt.timestamp() * 1000)
dt = datetime.fromtimestamp(millis / 1000, tz=timezone.utc)
