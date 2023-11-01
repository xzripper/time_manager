<h1 align="center">Time_Manager.</h1>
<p align="center">Improves work with time.</p>
<p align="center"><code>pip install pytime_manager</code></p>

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

# Blocking Time Thread VS Time Thread.
blocking_time_thread(do(lambda: print('Hello 1'), 1, 5)) # Uses virtual 'main' thread.

print('Application thread is unblocked but still unable to call blocking another time thread.')

blocking_time_thread(do(lambda: print('Hello 2 (Not going to print because its blocked for me)'), 1, 5)) # Uses virtual 'main' thread.

blocking_time_thread(do(lambda: print('Hello 3 (I\'m from another thread so I don\'t care.)'), 1, 5), thread='other_thread') # Uses virtual 'other_thread' thread.

time_thread(do(lambda: print('I\'m going to be printed because i\'m free time thread.'), 1, 5))

# Schedule function calling.
time_thread(
 do_every(
    lambda: print('Hello!'),

    [(1, MINUTE), (30, SECOND), (2.5, SECOND)], # 1min 32.5s (92.5s) [example: [(1, DAY), (12, HOUR)] => 1 day, 12 hours].

    False, # Once?

    translate_time # Needed for translating time. (import it from pytime_manager.uc).
 )
)
```

Adds more than 10 functions to improve work with time, and a lot more things.

<b>TimeManager <a href="https://github.com/xzripper/time_manager/blob/main/time_manager/__init__.py">Cheatsheet</a>.<br>
UnitConverter <a href="https://github.com/xzripper/time_manager/blob/main/time_manager/uc.py">Cheatsheet</a>.</b>
