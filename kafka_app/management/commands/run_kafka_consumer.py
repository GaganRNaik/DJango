from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
import json

class Command(BaseCommand):
    help = 'Run Kafka Consumer'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting Kafka Consumer..."))
        consumer = KafkaConsumer(
            'stock_price',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='django-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

        for message in consumer:
            # topic_name = message.topic
            self.stdout.write(f"Received message:{message}")
