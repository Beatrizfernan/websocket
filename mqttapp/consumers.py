import json
import paho.mqtt.client as mqtt
from channels.generic.websocket import WebsocketConsumer

# Criação do cliente MQTT usando a biblioteca Paho
mqtt_client = mqtt.Client()

# Configuração do broker MQTT e da porta de conexão
BROKER = 'broker.hivemq.com'
PORT = 8000

# Conexão ao broker MQTT
mqtt_client.connect(BROKER, PORT)

# Definição da classe PublishConsumer, que é um consumidor WebSocket para publicar mensagens
class PublishConsumer(WebsocketConsumer):
    def connect(self):
        # Aceita a conexão WebSocket quando um cliente se conecta
        self.accept()

    def disconnect(self, close_code):
        # Método de desconexão (nada a fazer aqui, mas precisa ser definido)
        pass

    def receive(self, text_data):
        # Método chamado quando uma mensagem é recebida pelo WebSocket
        data = json.loads(text_data)  # Converte a string JSON em um dicionário Python
        topic = data['topic']  # Extrai o tópico da mensagem
        message = data['message']  # Extrai a mensagem

        # Publica a mensagem no tópico especificado usando o cliente MQTT
        mqtt_client.publish(topic, message)
        print(f"Published message: {message} on topic: {topic}")  # Log da publicação

# Definição da classe SubscribeConsumer, que é um consumidor WebSocket para subscrever a tópicos e receber mensagens
class SubscribeConsumer(WebsocketConsumer):
    def connect(self):
        # Aceita a conexão WebSocket quando um cliente se conecta
        self.accept()

    def disconnect(self, close_code):
        # Método de desconexão (nada a fazer aqui, mas precisa ser definido)
        pass

    def receive(self, text_data):
        # Método chamado quando uma mensagem é recebida pelo WebSocket
        data = json.loads(text_data)  # Converte a string JSON em um dicionário Python
        topic = data['topic']  # Extrai o tópico da mensagem

        # Subscreve ao tópico especificado usando o cliente MQTT
        mqtt_client.subscribe(topic)

        # Define a função de callback que será chamada quando uma mensagem for recebida no tópico subscrito
        def on_message(client, userdata, msg):
            # Envia a mensagem recebida de volta ao cliente WebSocket
            self.send(text_data=json.dumps({
                'topic': msg.topic,
                'message': msg.payload.decode()
            }))

        # Configura o callback de mensagem do cliente MQTT
        mqtt_client.on_message = on_message
        # Inicia o loop do cliente MQTT para processar as mensagens recebidas
        mqtt_client.loop_start()
