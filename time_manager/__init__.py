"""Time Manager for Python."""

from time import sleep, perf_counter, perf_counter_ns, timezone as _timezone

from datetime import datetime

from pytz import timezone as _get_timezone

from threading import Thread

from typing import Union, Callable


TM_VERSION = 1.7

TimeUnit = int

TimeProcess = Callable[[], None]

Threads = dict[str, list[Thread]]

DelayT = list[tuple[Union[int, float], TimeUnit]]

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

m_time_zone: int = _timezone

m_get_timezone: Callable = _get_timezone

m_translate_time: Callable[[float, TimeUnit, TimeUnit], float] = None

def set_translate_time(_translate_time: Callable) -> None:
    """Set translate time function."""
    global m_translate_time

    m_translate_time = _translate_time

class WhileState:
    state: bool = True

    def restart(self) -> None:
        """Restart state."""
        self.state = True

    def stop(self) -> None:
        """Stop while loop."""
        self.state = False

class Delay:
    delay: DelayT = None

    def __init__(self, *delay: DelayT) -> None:
        """Create new delay."""
        self.delay = [*delay]

    def sum(self, to: TimeUnit=SECOND) -> float:
        """Convert delay to specific time unit."""
        return sum([m_translate_time(time[0], time[1], to) for time in self.delay])

    @staticmethod
    def get(delay: 'AdvancedDelayOrSimpleDelay', to: TimeUnit=SECOND) -> float:
        """Convert delay or just return delay if not advanced delay."""
        if isinstance(delay, Delay):
            return delay.sum(to)

        elif isinstance(delay, float) or isinstance(delay, int):
            return delay

AdvancedDelayOrSimpleDelay = Union[float, Delay]

threads: Threads = {MAIN_THREAD: []}

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

def wait(delay: AdvancedDelayOrSimpleDelay) -> None:
    """Wait (sleep)."""
    sleep(Delay.get(delay))

def do_and_wait(callable: Callable, delay: AdvancedDelayOrSimpleDelay) -> None:
    """Call callable and wait."""
    callable()

    wait(Delay.get(delay))

def call_after(callable: Callable, delay: AdvancedDelayOrSimpleDelay) -> TimeProcess:
    """Call function after delay."""
    return lambda: [wait(Delay.get(delay)), callable()]

def call_after2(callable1: Callable, callable2: Callable, delay: AdvancedDelayOrSimpleDelay) -> TimeProcess:
    """Call callable1, call callable2 after delay."""
    return lambda: [callable1(), wait(Delay.get(delay)), callable2()]

def do(callable: Callable, delay: AdvancedDelayOrSimpleDelay, times: int) -> TimeProcess:
    """Call callable X times."""
    def _process():
        for _ in range(times):
            callable()

            wait(Delay.get(delay))

    return _process

def do_for(callable: Callable, do_seconds: AdvancedDelayOrSimpleDelay) -> TimeProcess:
    """Call callable for some time."""
    def _process():
        passed = 0

        while passed <= Delay.get(do_seconds):
            before_callable = perf_counter()

            callable()

            passed += perf_counter() - before_callable

    return _process

def do_inf(callable: Callable, delay: AdvancedDelayOrSimpleDelay=0.0) -> TimeProcess:
    """Call callable infinity times."""
    def inf_proc():
        while True:
            callable()

            wait(Delay.get(delay))

    return inf_proc

def do_while(callable: Callable, state: WhileState, delay: AdvancedDelayOrSimpleDelay=0.0) -> TimeProcess:
    """Call callable while state is true."""
    def process():
        while state.state:
            callable()

            wait(Delay.get(delay))

    return process

def do_every(callable: Callable, delay: AdvancedDelayOrSimpleDelay, once: bool=False) -> TimeProcess:
    """Call callable after every delay, stop if 'once' is True."""
    def process():
        while True:
            wait(Delay.get(delay))

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

def utc(ms: bool=False) -> int:
    """Get UTC."""
    return int(datetime.now(getattr(__import__('datetime'), 'timezone').utc).timestamp() * (1000 if ms else 1))

def now(timezone: str=None) -> datetime:
    """Get current date and time (datetime)."""
    return datetime.now(m_get_timezone(timezone) if timezone else None)

def now_time(timezone: str=None) -> datetime:
    """Get current time (datetime)."""
    return now(timezone).time()

def dformat(time: datetime=None, _format: str='') -> datetime:
    """Format datetime."""
    return datetime.strptime(datetime.strftime(time if time else now(), _format), _format)

def sformat(time: datetime=None, _format: str='') -> str:
    """Format datetime and get formated date as string."""
    return datetime.strftime(time if time else now(), _format)
