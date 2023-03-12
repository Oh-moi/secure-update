#!/usr/bin/env python

from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from api import start_rest
from consumer import start_consumer
from multiprocessing import Queue

if __name__ == "__main__":
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()
    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md

    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])
    config.update(config_parser['fdp_output'])

    events_queue = Queue()
    events_queue_al = Queue()
    events_queue_aa = Queue()
    events_queue_up = Queue()
  
    start_rest(events_queue, events_queue_al, events_queue_aa, events_queue_up)
    start_consumer(args, config, events_queue, events_queue_al, events_queue_aa, events_queue_up)

