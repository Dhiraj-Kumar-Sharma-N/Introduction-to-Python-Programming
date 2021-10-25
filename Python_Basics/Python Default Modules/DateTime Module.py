"""

NAME
    datetime - Fast implementation of the datetime type.

CLASSES
    builtins.object
        date
            datetime
        time
        timedelta
        tzinfo
            timezone

    class date(builtins.object)
     |  date(year, month, day) --> date object
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __format__(...)
     |      Formats self with strftime.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  ctime(...)
     |      Return ctime() style string.
     |
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |
     |  isoformat(...)
     |      Return string in ISO 8601 format, YYYY-MM-DD.
     |
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |
     |  replace(...)
     |      Return date with new specified fields.
     |
     |  strftime(...)
     |      format -> strftime() style string.
     |
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  fromisoformat(...) from builtins.type
     |      str -> Construct a date from the output of date.isoformat()
     |
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |
     |  fromtimestamp(...) from builtins.type
     |      timestamp -> local date from a POSIX timestamp (like time.time()).
     |
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  day
     |
     |  month
     |
     |  year
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  max = datetime.date(9999, 12, 31)
     |
     |  min = datetime.date(1, 1, 1)
     |
     |  resolution = datetime.timedelta(days=1)

    class datetime(date)
     |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
     |
     |  The year, month and day arguments are required. tzinfo may be None, or an
     |  instance of a tzinfo subclass. The remaining arguments may be ints.
     |
     |  Method resolution order:
     |      datetime
     |      date
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  astimezone(...)
     |      tz -> convert to local time in new timezone tz
     |
     |  ctime(...)
     |      Return ctime() style string.
     |
     |  date(...)
     |      Return date object with same year, month and day.
     |
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |
     |  isoformat(...)
     |      [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |      sep is used to separate the year from the time, and defaults to 'T'.
     |      timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').
     |
     |  replace(...)
     |      Return datetime with new specified fields.
     |
     |  time(...)
     |      Return time object with same time but with tzinfo=None.
     |
     |  timestamp(...)
     |      Return POSIX timestamp as float.
     |
     |  timetuple(...)
     |      Return time tuple, compatible with time.localtime().
     |
     |  timetz(...)
     |      Return time object with same time and tzinfo.
     |
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |
     |  utctimetuple(...)
     |      Return UTC time tuple, compatible with time.localtime().
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  combine(...) from builtins.type
     |      date, time -> datetime with same date and time fields
     |
     |  fromisoformat(...) from builtins.type
     |      string -> datetime from datetime.isoformat() output
     |
     |  fromtimestamp(...) from builtins.type
     |      timestamp[, tz] -> tz's local time from POSIX timestamp.
     |
     |  now(tz=None) from builtins.type
     |      Returns new datetime object representing current time local to tz.
     |
     |        tz
     |          Timezone object.
     |
     |      If no tz is specified, uses local timezone.
     |
     |  strptime(...) from builtins.type
     |      string, format -> new datetime parsed from a string (like time.strptime()).
     |
     |  utcfromtimestamp(...) from builtins.type
     |      Construct a naive UTC datetime from a POSIX timestamp.
     |
     |  utcnow(...) from builtins.type
     |      Return a new datetime representing UTC day and time.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  fold
     |
     |  hour
     |
     |  microsecond
     |
     |  minute
     |
     |  second
     |
     |  tzinfo
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
     |
     |  min = datetime.datetime(1, 1, 1, 0, 0)
     |
     |  resolution = datetime.timedelta(microseconds=1)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from date:
     |
     |  __format__(...)
     |      Formats self with strftime.
     |
     |  isocalendar(...)
     |      Return a 3-tuple containing ISO year, week number, and weekday.
     |
     |  isoweekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 1 ... Sunday == 7
     |
     |  strftime(...)
     |      format -> strftime() style string.
     |
     |  toordinal(...)
     |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
     |
     |  weekday(...)
     |      Return the day of the week represented by the date.
     |      Monday == 0 ... Sunday == 6
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from date:
     |
     |  fromordinal(...) from builtins.type
     |      int -> date corresponding to a proleptic Gregorian ordinal.
     |
     |  today(...) from builtins.type
     |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from date:
     |
     |  day
     |
     |  month
     |
     |  year

    class time(builtins.object)
     |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
     |
     |  All arguments are optional. tzinfo may be None, or an instance of
     |  a tzinfo subclass. The remaining arguments may be ints.
     |
     |  Methods defined here:
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __format__(...)
     |      Formats self with strftime.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |
     |  __reduce_ex__(...)
     |      __reduce_ex__(proto) -> (cls, state)
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  dst(...)
     |      Return self.tzinfo.dst(self).
     |
     |  isoformat(...)
     |      Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
     |
     |      timespec specifies what components of the time to include.
     |
     |  replace(...)
     |      Return time with new specified fields.
     |
     |  strftime(...)
     |      format -> strftime() style string.
     |
     |  tzname(...)
     |      Return self.tzinfo.tzname(self).
     |
     |  utcoffset(...)
     |      Return self.tzinfo.utcoffset(self).
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  fromisoformat(...) from builtins.type
     |      string -> time from time.isoformat() output
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  fold
     |
     |  hour
     |
     |  microsecond
     |
     |  minute
     |
     |  second
     |
     |  tzinfo
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  max = datetime.time(23, 59, 59, 999999)
     |
     |  min = datetime.time(0, 0)
     |
     |  resolution = datetime.timedelta(microseconds=1)

    class timedelta(builtins.object)
     |  Difference between two datetime values.
     |
     |  timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
     |
     |  All arguments are optional and default to 0.
     |  Arguments may be integers or floats, and may be positive or negative.
     |
     |  Methods defined here:
     |
     |  __abs__(self, /)
     |      abs(self)
     |
     |  __add__(self, value, /)
     |      Return self+value.
     |
     |  __bool__(self, /)
     |      self != 0
     |
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __mod__(self, value, /)
     |      Return self%value.
     |
     |  __mul__(self, value, /)
     |      Return self*value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __neg__(self, /)
     |      -self
     |
     |  __pos__(self, /)
     |      +self
     |
     |  __radd__(self, value, /)
     |      Return value+self.
     |
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |
     |  __reduce__(...)
     |      __reduce__() -> (cls, state)
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |
     |  __rmod__(self, value, /)
     |      Return value%self.
     |
     |  __rmul__(self, value, /)
     |      Return value*self.
     |
     |  __rsub__(self, value, /)
     |      Return value-self.
     |
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  __sub__(self, value, /)
     |      Return self-value.
     |
     |  __truediv__(self, value, /)
     |      Return self/value.
     |
     |  total_seconds(...)
     |      Total seconds in the duration.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  days
     |      Number of days.
     |
     |  microseconds
     |      Number of microseconds (>= 0 and less than 1 second).
     |
     |  seconds
     |      Number of seconds (>= 0 and less than 1 day).
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  max = datetime.timedelta(days=999999999, seconds=86399, microseconds=9...
     |
     |  min = datetime.timedelta(days=-999999999)
     |
     |  resolution = datetime.timedelta(microseconds=1)

    class timezone(tzinfo)
     |  Fixed offset from UTC implementation of tzinfo.
     |
     |  Method resolution order:
     |      timezone
     |      tzinfo
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __eq__(self, value, /)
     |      Return self==value.
     |
     |  __ge__(self, value, /)
     |      Return self>=value.
     |
     |  __getinitargs__(...)
     |      pickle support
     |
     |  __gt__(self, value, /)
     |      Return self>value.
     |
     |  __hash__(self, /)
     |      Return hash(self).
     |
     |  __le__(self, value, /)
     |      Return self<=value.
     |
     |  __lt__(self, value, /)
     |      Return self<value.
     |
     |  __ne__(self, value, /)
     |      Return self!=value.
     |
     |  __repr__(self, /)
     |      Return repr(self).
     |
     |  __str__(self, /)
     |      Return str(self).
     |
     |  dst(...)
     |      Return None.
     |
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |
     |  tzname(...)
     |      If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'.
     |
     |  utcoffset(...)
     |      Return fixed offset.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  max = datetime.timezone(datetime.timedelta(seconds=86340))
     |
     |  min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
     |
     |  utc = datetime.timezone.utc
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from tzinfo:
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      -> (cls, state)

    class tzinfo(builtins.object)
     |  Abstract base class for time zone info objects.
     |
     |  Methods defined here:
     |
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |
     |  __reduce__(...)
     |      -> (cls, state)
     |
     |  dst(...)
     |      datetime -> DST offset as timedelta positive east of UTC.
     |
     |  fromutc(...)
     |      datetime in UTC -> datetime in local time.
     |
     |  tzname(...)
     |      datetime -> string name of time zone.
     |
     |  utcoffset(...)
     |      datetime -> timedelta showing offset from UTC, negative values indicating West of UTC
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

DATA
    MAXYEAR = 9999
    MINYEAR = 1
    datetime_CAPI = <capsule object "datetime.datetime_CAPI">


"""

import datetime
import pytz

print(datetime.date.today())  # 2021-09-14

print(datetime.date.isoweekday(datetime.date.today()))  # 2

print(datetime.date.isocalendar(datetime.date.today()))  # (2021, 37, 2)

print(datetime.date.isoformat(datetime.date.today()))  # 2021-09-14

test_date = '4/25/2015'
dt_obj = datetime.datetime.strptime(test_date, '%m/%d/%Y')

print(datetime.datetime.strftime(dt_obj, '%Y-%m-%d %H:%M:%S'))  # 2015-04-25 00:00:00

print(datetime.date.weekday(datetime.date.today()))  # 1

print(datetime.date.max)  # 9999-12-31

print(datetime.datetime.today())  # 2021-09-14 09:49:13.339648

print(datetime.datetime.now())  # 2021-09-14 09:49:13.339648

print(datetime.datetime.now().year)  # 2021

print(datetime.datetime.now().month)  # 9

print(datetime.datetime.now().day)  # 14

print(datetime.datetime.now().hour)  # 9

print(datetime.datetime.now().minute)  # 57

print(datetime.datetime.now().strftime('%Y-%m-%d'))  # 2021-09-14

print(datetime.datetime.now().strftime('%y-%m-%d'))  # 21-09-14

print(datetime.datetime.now().strftime('%m-%d'))  # 09-14

print(datetime.datetime.now().strftime('%c'))  # Tue Sep 14 09:59:13 2021

# for Different Time Zone

print(pytz.all_timezones)

CST = pytz.timezone('US/Pacific')
AFR = pytz.timezone('Africa/Accra')
print(datetime.datetime.now(CST))  # 2021-09-13 21:23:09.238628-07:00
print(datetime.datetime.now(AFR))  # 2021-09-14 04:24:54.302606+00:00

print(type(CST))  # <class 'pytz.tzfile.US/Pacific'>

print(datetime.datetime.fromtimestamp(1555555))  # 1970-01-19 05:35:55


