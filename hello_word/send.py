import pika

# Criando um canal de conexão
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criando/Declarando uma fila
channel.queue_declare(queue='hello')

# Enviando a mensagem(body) para uma exchange vazia 
# onde a routing key é o nome da fila
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

# Printa a mensagem que foi enviada
print(" [x] Sent 'Hello World!'")

# Fecha a conexao
connection.close()