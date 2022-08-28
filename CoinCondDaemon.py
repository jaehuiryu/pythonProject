import sys
import os
import time
import daemon from daemon import pidfile

def do_something():
    while True:
        time.sleep(1)

def start_daemon():
    print('start daemon')

def main():
    try:
        if sys.argv[1] == 'start':
            start_daemon()
        elif sys.argv[1] == 'stop':
            
