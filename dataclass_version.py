import time
from dataclasses import dataclass,field
from typing import Optional
@dataclass
class Timer:
    _start_time: Optional[float] = field(default=None, init=False, repr=False)
    text: str = "Elapsed Time: {:0.4f} seconds"
    logger: str = print

    def start(self):
        """Start the timer"""
        self._start_time  = time.perf_counter()
    
    def stop(self):
        """Stop the timer and print Elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))

def main():
    """Calculate time taken for 100000 loop"""
    t = Timer()
    t.start()
    for i in range(100000):
        pass
    t.stop()
    
if __name__ == "__main__":
    main()
 
    