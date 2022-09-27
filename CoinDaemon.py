import sys
import os
import time
import daemon
from daemon import pidfile
import logging
from logging import handlers

pid_file = '/Users/apple/PycharmProjects/pythonProject/coindaemon.pid'
log_file = '/Users/apple/PycharmProjects/pythonProject/coindaemon.log'
_logger = logging.getLogger("mylogger")
_logger.setLevel(logging.INFO)
_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def do_something():
    _logger.info('do_somethin start')
    while True:
        _logger.info('while do_something')
        time.sleep(2)

def start_daemon():
    print('start_daemon')
    file_handler = handlers.RotatingFileHandler(
        log_file,
        maxBytes=(1024 * 1024),
        backupCount=3
    )
    file_handler.setFormatter(_formatter)
    _logger.addHandler(file_handler)
    _logger.info('log start')
    context = daemon.DaemonContext(
        working_directory = '/tmp',
        umask = 0o002,
        pidfile = pidfile.TimeoutPIDLockFile(pid_file),
        )
        #logfile_fileno=file_handler.stream.fileno()
    context.files_preserve = [file_handler.stream]
    _logger.info('step1')
    with context:
        do_something()

def main():
    try:
        if sys.argv[1] == 'start':
            start_daemon()

        elif sys.argv[1] == 'stop':
            pid = '999999'

            f = open(pid_file, 'r')

            for line in f:
                pid = line = line.strip()

            f.close()

            cmd = 'kill '+ pid

            os.system(cmd)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()