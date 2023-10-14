<h1 align="center">Time_Manager.</h1>
<p align="center">Improves work with time.</p>

```python
# Time Manager.
from time_manager import *
from time_manager.uc import *


# Translate one year into days.
print(translate_time(1, YEAR, DAY)) # => 365

# Or...
print(translate_time_y(1, DAY)) # => 365

# Print 'Hello!' after three seconds.
time_thread(
    call_after(
        lambda: print('Hello!'),
        3
    )
)

# Print 'Hello!' and after three seconds print 'Bye!'.
time_thread(
    call_after2(
        lambda: print('Hello!'),
        lambda: print('Bye!'),
        3
    )
)

# Print message for three seconds.
time_thread(
    do_for(
        lambda: print('Print me for three seconds.'),
        3
    )
)

# Print message three times with one second delay.
time_thread(
    do(
        lambda: print('print me 3 times with one second delay'), 1, 3
    )
)

# Print message and wait three seconds.
do_and_wait(lambda: print('Hi!'), 3)
```

Adds more than 10 functions to improve work with time, and a lot more things.

<b>TimeManager <a href="https://github.com/xzripper/time_manager/blob/main/time_manager/__init__.py">Cheatsheet</a>.<br>
UnitConverter <a href="https://github.com/xzripper/time_manager/blob/main/time_manager/uc.py">Cheatsheet</a>.</b>
