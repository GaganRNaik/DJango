from kafka import KafkaProducer
import json
import requests
import yfinance as yf

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period="1d")  # Get the latest stock data for today
    return stock_data.tail(1).to_dict(orient='records')[0] 


def send_message(stock):
    stock_data = get_stock_data(stock)
    producer.send(f"stock_price", stock_data)
    producer.flush()
