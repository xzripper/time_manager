"""Unit Converter."""

from . import Union, TimeUnit, NANOSECOND, MICROSECOND, MILLISECOND, SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, YEAR, TM_VERSION


def translate_time_ns(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate nanoseconds to other unit."""
    if unit == NANOSECOND: return time
    elif unit == MICROSECOND: return time / 1000
    elif unit == MILLISECOND: return time / 1e+6
    elif unit == SECOND: return time / 1e+9
    elif unit == MINUTE: return time / 6e+10
    elif unit == HOUR: return time / 3.6e+12
    elif unit == DAY: return time / 8.64e+13
    elif unit == WEEK: return time / 6.048e+14
    elif unit == MONTH: return time / 2.628e+15
    elif unit == YEAR: return time / 3.154e+16
    else: return time

def translate_time_mis(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate microseconds to other unit."""
    if unit == NANOSECOND: return time * 1000
    elif unit == MICROSECOND: return time
    elif unit == MILLISECOND: return time / 1000
    elif unit == SECOND: return time / 1e+6
    elif unit == MINUTE: return time / 6e+7
    elif unit == HOUR: return time / 3.6e+9
    elif unit == DAY: return time / 8.64e+10
    elif unit == WEEK: return time / 6.048e+11
    elif unit == MONTH: return time / 2.628e+12
    elif unit == YEAR: return time / 3.154e+13
    else: return time

def translate_time_ms(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate milliseconds to other unit."""
    if unit == NANOSECOND: return time * 1e+6
    elif unit == MICROSECOND: return time * 1000
    elif unit == MILLISECOND: return time
    elif unit == SECOND: return time / 1000
    elif unit == MINUTE: return time / 60000
    elif unit == HOUR: return time / 3.6e+6
    elif unit == DAY: return time / 8.64e+7
    elif unit == WEEK: return time / 6.048e+8
    elif unit == MONTH: return time / 2.628e+9
    elif unit == YEAR: return time / 3.154e+10
    else: return time

def translate_time_s(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate seconds to other unit."""
    if unit == NANOSECOND: return time * 1e+9
    elif unit == MICROSECOND: return time * 1e+6
    elif unit == MILLISECOND: return time * 1000
    elif unit == SECOND: return time
    elif unit == MINUTE: return time / 60
    elif unit == HOUR: return time / 3600
    elif unit == DAY: return time / 86400
    elif unit == WEEK: return time / 604800
    elif unit == MONTH: return time / 2.628e+6
    elif unit == YEAR: return time / 3.154e+7
    else: return time

def translate_time_m(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate minutes to other unit."""
    if unit == NANOSECOND: return time * 3.6e+12
    elif unit == MICROSECOND: return time * 6e+7
    elif unit == MILLISECOND: return time * 60000
    elif unit == SECOND: return time * 60
    elif unit == MINUTE: return time
    elif unit == HOUR: return time / 60
    elif unit == DAY: return time / 1440
    elif unit == WEEK: return time / 10080
    elif unit == MONTH: return time / 43800
    elif unit == YEAR: return time / 525600
    else: return time

def translate_time_h(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate hour to other unit."""
    if unit == NANOSECOND: return time * 3.6e+12
    elif unit == MICROSECOND: return time * 3.6e+9
    elif unit == MILLISECOND: return time * 3.6e+6
    elif unit == SECOND: return time * 3600
    elif unit == MINUTE: return time * 60
    elif unit == HOUR: return time
    elif unit == DAY: return time / 24
    elif unit == WEEK: return time / 168
    elif unit == MONTH: return time / 730
    elif unit == YEAR: return time / 8760
    else: return time

def translate_time_d(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate day to other unit."""
    if unit == NANOSECOND: return time * 8.64e+13
    elif unit == MICROSECOND: return time * 8.64e+10
    elif unit == MILLISECOND: return time * 8.64e+7
    elif unit == SECOND: return time * 86400
    elif unit == MINUTE: return time * 1440
    elif unit == HOUR: return time * 24
    elif unit == DAY: return time
    elif unit == WEEK: return time / 7
    elif unit == MONTH: return time / 30.417
    elif unit == YEAR: return time / 365
    else: return time

def translate_time_w(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate week to other unit."""
    if unit == NANOSECOND: return time * 6.048e+14
    elif unit == MICROSECOND: return time * 6.048e+11
    elif unit == MILLISECOND: return time * 6.048e+8
    elif unit == SECOND: return time * 604800
    elif unit == MINUTE: return time * 10080
    elif unit == HOUR: return time * 168
    elif unit == DAY: return time * 7
    elif unit == WEEK: return time
    elif unit == MONTH: return time / 4.345
    elif unit == YEAR: return time / 52.143
    else: return time

def translate_time_mo(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate month to other unit."""
    if unit == NANOSECOND: return time * 2.628e+15
    elif unit == MICROSECOND: return time * 2.628e+12
    elif unit == MILLISECOND: return time * 2.628e+9
    elif unit == SECOND: return time * 2.628e+6
    elif unit == MINUTE: return time * 43800
    elif unit == HOUR: return time * 730
    elif unit == DAY: return time * 30.417
    elif unit == WEEK: return time * 4.345
    elif unit == MONTH: return time
    elif unit == YEAR: return time / 12
    else: return time

def translate_time_y(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate year to other unit."""
    if unit == NANOSECOND: return time * 3.154e+16
    elif unit == MICROSECOND: return time * 3.154e+13
    elif unit == MILLISECOND: return time * 3.54e+10
    elif unit == SECOND: return time * 3.154e+7
    elif unit == MINUTE: return time * 525600
    elif unit == HOUR: return time * 8760
    elif unit == DAY: return time * 365
    elif unit == WEEK: return time * 52.143
    elif unit == MONTH: return time * 12
    elif unit == YEAR: return time
    else: return time

def translate_time(time: float, time_unit: TimeUnit, convert_to: TimeUnit) -> Union[int, float]:
    """Translate one unit to another."""
    if time_unit == convert_to: return time
    elif time_unit == NANOSECOND: return translate_time_ns(time, convert_to)
    elif time_unit == MICROSECOND: return translate_time_mis(time, convert_to)
    elif time_unit == MILLISECOND: return translate_time_ms(time, convert_to)
    elif time_unit == SECOND: return translate_time_s(time, convert_to)
    elif time_unit == MINUTE: return translate_time_m(time, convert_to)
    elif time_unit == HOUR: return translate_time_h(time, convert_to)
    elif time_unit == DAY: return translate_time_d(time, convert_to)
    elif time_unit == WEEK: return translate_time_w(time, convert_to)
    elif time_unit == YEAR: return translate_time_y(time, convert_to)
    else: return time
