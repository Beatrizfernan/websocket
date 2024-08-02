import json
import paho.mqtt.client as mqtt
from channels.generic.websocket import WebsocketConsumer

mqtt_client = mqtt.Client()

BROKER = 'broker.hivemq.com'
PORT = 8000

mqtt_client.connect(BROKER, PORT)

class PublishConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        topic = data['topic']
        message = data['message']
        
        mqtt_client.publish(topic, message)
        print(f"Published message: {message} on topic: {topic}")

class SubscribeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        topic = data['topic']
        
        mqtt_client.subscribe(topic)

        def on_message(client, userdata, msg):
            self.send(text_data=json.dumps({
                'topic': msg.topic,
                'message': msg.payload.decode()
            }))

        mqtt_client.on_message = on_message
        mqtt_client.loop_start()
