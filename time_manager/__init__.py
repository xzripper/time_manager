"""Time Manager for Python."""

from time import sleep, perf_counter, perf_counter_ns

from threading import Thread

from typing import Union, Callable


TM_VERSION = 1.6_2

TimeUnit = int

TimeProcess = Callable[[], None]

Threads = dict[str, list[Thread]]

Date = list[tuple[int, TimeUnit]]

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

MAIN_THREAD: str = 'main'

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

threads: Threads = {'main': []}

def time_thread(time_process: TimeProcess, daemon: bool=False) -> None:
    """Run time process in a thread."""
    Thread(target=time_process, daemon=daemon).start()

def blocking_time_thread(time_process: TimeProcess, daemon: bool=False, thread: str=MAIN_THREAD) -> None:
    """Run time process in a blocking thread. If any thread running in thread queue, this thread will not be added to queue and executed."""
    if thread not in threads.keys():
        threads[thread] = []

    if all(not _thread.is_alive() for _thread in threads[thread]):
        thread_o = Thread(target=time_process, daemon=daemon)

        thread_o.start()

        threads[thread].append(thread_o)

def do_process(time_process: TimeProcess) -> None:
    """Run time process without thread."""
    time_process()

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

def do_inf(callable: Callable, delay: float=0.0) -> TimeProcess:
    """Call callable infinity times."""
    def inf_proc():
        while True:
            callable()

            wait(delay)

    return inf_proc

def do_while(callable: Callable, state: WhileState, delay: float=0.0) -> TimeProcess:
    """Call callable while state is true."""
    def process():
        while state.state:
            callable()

            wait(delay)

    return process

def do_every(callable: Callable, delay: Date, once: bool=False, _time_translate: Callable='NON-OPTIONAL') -> TimeProcess:
    """Call callable after every delay, stop if 'once' is True."""
    if isinstance(_time_translate, str):
        return lambda: print('_time_translate is not specified [do_every].')

    def process():
        while True:
            wait(sum([_time_translate(time[0], time[1], SECOND) for time in delay]))

            callable()

            if once:
                break

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
