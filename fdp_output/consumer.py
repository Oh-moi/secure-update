# implements Kafka topic consumer functionality

import multiprocessing
import threading
from confluent_kafka import Consumer, OFFSET_BEGINNING
import json



_events_queue: multiprocessing.Queue or None = None
_events_queu_al: multiprocessing.Queue or None = None


def handle_event(id: str, details: dict):
    print(f"[info] handling event {id}, {details['source']}->{details['deliver_to']}: {details['operation']}")
    if details['operation'] == 'process_new_auth':
        _events_queue.put(details)
    elif details['operation'] == 'process_new_events':
        _events_queue_al.put(details)
    elif details['operation'] == 'process_new_data':
        _events_queue_aa.put(details)
    elif details['operation'] == 'process_update_delivery':
        _events_queue_up.put(details)
        

def consumer_job(args, config, events_queue=None, events_queue_al=None, events_queue_aa=None, events_queue_up=None):

    global _events_queue
    _events_queue = events_queue

    global _events_queue_al
    _events_queue_al = events_queue_al

    global _events_queue_aa
    _events_queue_aa = events_queue_aa

    global _events_queue_up
    _events_queue_up = events_queue_up

    # Create Consumer instance
    manager_consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    def reset_offset(manager_consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            manager_consumer.assign(partitions)

    # Subscribe to topic
    topic = "fdp_output"
    manager_consumer.subscribe([topic], on_assign=reset_offset)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = manager_consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                # print("Waiting...")
                pass
            elif msg.error():
                print(f"[error] {msg.error()}")
            else:
                try:
                    id = msg.key().decode('utf-8')
                    details = json.loads(msg.value().decode('utf-8'))
                    handle_event(id, details)
                except Exception as e:
                    print(
                        f"[error] malformed event received from topic {topic}: {msg.value()}. {e}")    
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        manager_consumer.close()

def start_consumer(args, config, events_queue, events_queue_al, events_queue_aa, events_queue_up):
    threading.Thread(target=lambda: consumer_job(args, config, events_queue, events_queue_al, events_queue_aa, events_queue_up)).start()
    
if __name__ == '__main__':
    start_consumer(None)
 