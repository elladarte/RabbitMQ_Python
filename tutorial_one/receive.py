import pika, sys, os

def main():
    # Criando um canal de conexão
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Cria/Declara a fila
    # é uma boa pratica a ser feita para nao correr o risco 
    # da mensagem ser descartada
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        # Função responsavel por imprimir na tera a mensagem recebida

        print(" [x] Received %r" % body)

    # Definimos os paramentos em qual fila a mensagem deve ser consumida,
    # entramos em um loop sem fim que espera por dados e executa callbacks 
    # sempre que necessário e detecta KeyboardInterrupt durante o desligamento do programa
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    # Print que a mensagem foi consumida
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)