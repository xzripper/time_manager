"""Time Manager for Python."""

from time import sleep, perf_counter, perf_counter_ns

from threading import Thread

from typing import Union, Callable


TM_VERSION = 1.3

TimeUnit = int

TimeProcess = Callable[[], None]

NANOSECOND: TimeUnit = 1
MICROSECOND: TimeUnit = 2
MILLISECOND: TimeUnit = 3
SECOND: TimeUnit = 4
MINUTE: TimeUnit = 5
HOUR: TimeUnit = 6
DAY: TimeUnit = 7
WEEK: TimeUnit = 8
MONTH: TimeUnit = 9
YEAR: TimeUnit = 10

time_counter: Callable[[], float] = perf_counter
time_counter_ns: Callable[[], int] = perf_counter_ns

class WhileState:
    state: bool = True

    def restart(self) -> None:
        """Restart state."""
        self.state = True

    def stop(self) -> None:
        """Stop while loop."""
        self.state = False

def time_thread(time_process: TimeProcess, daemon: bool=False) -> None:
    """Run time process in a thread."""
    Thread(target=time_process, daemon=daemon).start()

def do_process(time_process: TimeProcess) -> None:
    """Run time process without thread."""
    time_process()

def t_round(number: float, round_float: bool=True) -> int:
    """
    Round number.

    `round_float` is True:
    ```
    t_round(5.75) # => 5
    t_round(1.0) # => 1
    ```

    `round_float` is False:
    ```
    t_round(5.75) # => 5.75
    t_round(1.0) # => 1

    t_round(456.4859) # => 456.4859
    t_round(456.0) # => 456
    """
    if round_float:
        return round(number)

    else:
        digits = str(number).split('.')

        if len(digits) > 1:
            if int(digits[1]) == 0:
                return round(number)

        else:
            return number

def wait(delay: float) -> None:
    """Wait (sleep)."""
    sleep(delay)

def do_and_wait(callable: Callable, delay: float) -> None:
    """Call callable and wait."""
    callable()

    wait(delay)

def call_after(callable: Callable, delay: float) -> TimeProcess:
    """Call function after delay."""
    return lambda: [wait(delay), callable()]

def call_after2(callable1: Callable, callable2: Callable, delay: float) -> TimeProcess:
    """Call callable1, call callable2 after delay."""
    return lambda: [callable1(), wait(delay), callable2()]

def do(callable: Callable, delay: float, times: int) -> TimeProcess:
    """Call callable X times."""
    def _process():
        for _ in range(times):
            callable()

            wait(delay)

    return _process

def do_for(callable: Callable, do_seconds: float) -> TimeProcess:
    """Call callable for some time."""
    def _process():
        passed = 0

        while passed <= do_seconds:
            before_callable = perf_counter()

            callable()

            passed += perf_counter() - before_callable

    return _process

def do_inf(callable: Callable) -> TimeProcess:
    """Call callable infinity times."""
    def inf_proc():
        while True:
            callable()

    return inf_proc

def do_while(callable: Callable, state: WhileState, delay: float=0.0) -> TimeProcess:
    """Call callable while state is true."""
    def process():
        while state.state:
            callable()

            wait(delay)

    return process

def code_exec_time(callable: Callable, ns: bool=False) -> float:
    """Get code execution time."""
    if ns:
        start = perf_counter_ns()

        callable()

        return perf_counter_ns() - start

    else:
        start = perf_counter()

        callable()

        return perf_counter() - start
