
import time, sys

def heart():
    frames = ["<3  ", "<33 ", "<333", "<33 ", "<3  "]
    for _ in range(2):
        for f in frames:
            sys.stdout.write("\r" + f)
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r   ")
