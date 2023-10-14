"""Unit Converter."""

from . import t_round, Union, TimeUnit, NANOSECOND, MICROSECOND, MILLISECOND, SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, YEAR, TM_VERSION


def translate_time_ns(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate nanoseconds to other unit."""
    if unit == NANOSECOND: return t_round(time, False)
    elif unit == MICROSECOND: return t_round(time / 1000, False)
    elif unit == MILLISECOND: return t_round(time / 1e+6, False)
    elif unit == SECOND: return t_round(time / 1e+9, False)
    elif unit == MINUTE: return t_round(time / 6e+10, False)
    elif unit == HOUR: return t_round(time / 3.6e+12, False)
    elif unit == DAY: return t_round(time / 8.64e+13, False)
    elif unit == WEEK: return t_round(time / 6.048e+14, False)
    elif unit == MONTH: return t_round(time / 2.628e+15, False)
    elif unit == YEAR: return t_round(time / 3.154e+16, False)
    else: return t_round(time, False)

def translate_time_mis(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate microseconds to other unit."""
    if unit == NANOSECOND: return t_round(time * 1000, False)
    elif unit == MICROSECOND: return t_round(time)
    elif unit == MILLISECOND: return t_round(time / 1000, False)
    elif unit == SECOND: return t_round(time / 1e+6, False)
    elif unit == MINUTE: return t_round(time / 6e+7, False)
    elif unit == HOUR: return t_round(time / 3.6e+9, False)
    elif unit == DAY: return t_round(time / 8.64e+10, False)
    elif unit == WEEK: return t_round(time / 6.048e+11, False)
    elif unit == MONTH: return t_round(time / 2.628e+12, False)
    elif unit == YEAR: return t_round(time / 3.154e+13, False)
    else: return t_round(time, False)

def translate_time_ms(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate milliseconds to other unit."""
    if unit == NANOSECOND: return t_round(time * 1e+6, False)
    elif unit == MICROSECOND: return t_round(time * 1000, False)
    elif unit == MILLISECOND: return t_round(time)
    elif unit == SECOND: return t_round(time / 1000, False)
    elif unit == MINUTE: return t_round(time / 60000, False)
    elif unit == HOUR: return t_round(time / 3.6e+6, False)
    elif unit == DAY: return t_round(time / 8.64e+7, False)
    elif unit == WEEK: return t_round(time / 6.048e+8, False)
    elif unit == MONTH: return t_round(time / 2.628e+9, False)
    elif unit == YEAR: return t_round(time / 3.154e+10, False)
    else: return t_round(time, False)

def translate_time_s(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate seconds to other unit."""
    if unit == NANOSECOND: return t_round(time * 1e+9, False)
    elif unit == MICROSECOND: return t_round(time * 1e+6, False)
    elif unit == MILLISECOND: return t_round(time * 1000, False)
    elif unit == SECOND: return t_round(time)
    elif unit == MINUTE: return t_round(time / 60, False)
    elif unit == HOUR: return t_round(time / 3600, False)
    elif unit == DAY: return t_round(time / 86400, False)
    elif unit == WEEK: return t_round(time / 604800, False)
    elif unit == MONTH: return t_round(time / 2.628e+6, False)
    elif unit == YEAR: return t_round(time / 3.154e+7, False)
    else: return t_round(time, False)

def translate_time_m(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate minutes to other unit."""
    if unit == NANOSECOND: return t_round(time * 3.6e+12, False)
    elif unit == MICROSECOND: return t_round(time * 6e+7, False)
    elif unit == MILLISECOND: return t_round(time * 60000, False)
    elif unit == SECOND: return t_round(time * 60, False)
    elif unit == MINUTE: return t_round(time)
    elif unit == HOUR: return t_round(time / 60, False)
    elif unit == DAY: return t_round(time / 1440, False)
    elif unit == WEEK: return t_round(time / 10080, False)
    elif unit == MONTH: return t_round(time / 43800, False)
    elif unit == YEAR: return t_round(time / 525600, False)
    else: return t_round(time, False)

def translate_time_h(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate hour to other unit."""
    if unit == NANOSECOND: return t_round(time * 3.6e+12, False)
    elif unit == MICROSECOND: return t_round(time * 3.6e+9, False)
    elif unit == MILLISECOND: return t_round(time * 3.6e+6, False)
    elif unit == SECOND: return t_round(time * 3600, False)
    elif unit == MINUTE: return t_round(time * 60, False)
    elif unit == HOUR: return t_round(time)
    elif unit == DAY: return t_round(time / 24, False)
    elif unit == WEEK: return t_round(time / 168, False)
    elif unit == MONTH: return t_round(time / 730, False)
    elif unit == YEAR: return t_round(time / 8760, False)
    else: return t_round(time, False)

def translate_time_d(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate day to other unit."""
    if unit == NANOSECOND: return t_round(time * 8.64e+13, False)
    elif unit == MICROSECOND: return t_round(time * 8.64e+10, False)
    elif unit == MILLISECOND: return t_round(time * 8.64e+7, False)
    elif unit == SECOND: return t_round(time * 86400, False)
    elif unit == MINUTE: return t_round(time * 1440, False)
    elif unit == HOUR: return t_round(time * 24, False)
    elif unit == DAY: return t_round(time)
    elif unit == WEEK: return t_round(time / 7, False)
    elif unit == MONTH: return t_round(time / 30.417, False)
    elif unit == YEAR: return t_round(time / 365, False)
    else: return t_round(time, False)

def translate_time_w(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate week to other unit."""
    if unit == NANOSECOND: return t_round(time * 6.048e+14, False)
    elif unit == MICROSECOND: return t_round(time * 6.048e+11, False)
    elif unit == MILLISECOND: return t_round(time * 6.048e+8, False)
    elif unit == SECOND: return t_round(time * 604800, False)
    elif unit == MINUTE: return t_round(time * 10080, False)
    elif unit == HOUR: return t_round(time * 168, False)
    elif unit == DAY: return t_round(time * 7, False)
    elif unit == WEEK: return t_round(time)
    elif unit == MONTH: return t_round(time / 4.345, False)
    elif unit == YEAR: return t_round(time / 52.143, False)
    else: return t_round(time, False)

def translate_time_mo(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate month to other unit."""
    if unit == NANOSECOND: return t_round(time * 2.628e+15, False)
    elif unit == MICROSECOND: return t_round(time * 2.628e+12, False)
    elif unit == MILLISECOND: return t_round(time * 2.628e+9, False)
    elif unit == SECOND: return t_round(time * 2.628e+6, False)
    elif unit == MINUTE: return t_round(time * 43800, False)
    elif unit == HOUR: return t_round(time * 730, False)
    elif unit == DAY: return t_round(time * 30.417, False)
    elif unit == WEEK: return t_round(time * 4.345, False)
    elif unit == MONTH: return t_round(time)
    elif unit == YEAR: return t_round(time / 12, False)
    else: return t_round(time, False)

def translate_time_y(time: float, unit: TimeUnit) -> Union[int, float]:
    """Translate year to other unit."""
    if unit == NANOSECOND: return t_round(time * 3.154e+16, False)
    elif unit == MICROSECOND: return t_round(time * 3.154e+13, False)
    elif unit == MILLISECOND: return t_round(time * 3.54e+10, False)
    elif unit == SECOND: return t_round(time * 3.154e+7, False)
    elif unit == MINUTE: return t_round(time * 525600, False)
    elif unit == HOUR: return t_round(time * 8760, False)
    elif unit == DAY: return t_round(time * 365, False)
    elif unit == WEEK: return t_round(time * 52.143, False)
    elif unit == MONTH: return t_round(time * 12, False)
    elif unit == YEAR: return t_round(time)
    else: return t_round(time, False)

def translate_time(time: float, time_unit: TimeUnit, convert_to: TimeUnit) -> Union[int, float]:
    """Translate one unit to another."""
    if time_unit == convert_to: return t_round(time, False)
    elif time_unit == NANOSECOND: return translate_time_ns(time, convert_to)
    elif time_unit == MICROSECOND: return translate_time_mis(time, convert_to)
    elif time_unit == MILLISECOND: return translate_time_ms(time, convert_to)
    elif time_unit == SECOND: return translate_time_s(time, convert_to)
    elif time_unit == MINUTE: return translate_time_m(time, convert_to)
    elif time_unit == HOUR: return translate_time_h(time, convert_to)
    elif time_unit == DAY: return translate_time_d(time, convert_to)
    elif time_unit == WEEK: return translate_time_w(time, convert_to)
    elif time_unit == YEAR: return translate_time_y(time, convert_to)
    else: return t_round(time, False)
