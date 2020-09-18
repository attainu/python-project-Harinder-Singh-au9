import time
import sys

class Banner:
    def print_banner(self,txt):
        for l in txt:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)

