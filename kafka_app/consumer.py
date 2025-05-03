from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='django-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def listen_to_messages():
    for message in consumer:
        print(f"Received: {message.value}")

