import time

class Timer:
    def __init__(self, text="Elapsed Time: {:0.4f} seconds", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger
    
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