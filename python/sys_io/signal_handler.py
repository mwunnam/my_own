#!/usr/bin/env python3

import sys
import signal

def signal_handler(sig, frame):
    print(f'Signal received is {sig}')
    print(f'Frame info: {frame}')
    print('You pressed CTRL + C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print('Press CTRL + C to exit')

while True:
    pass
