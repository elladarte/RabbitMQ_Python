# RabbitMQ

<p align="center">
<img src="https://www.rabbitmq.com/img/logo-rabbitmq.svg"/>
<img src="https://img.shields.io/static/v1?label=Status&message=Em_andamento&color=orange&style=for-the-badge"/>
</p>

## Introdução

É um software de enfilerameto de mensagens também conhecidos como intermediario de mensagens ou gerenciador de filas.
Uma mensagem pode incluir qualquer tipo de informação, dede de processos de tarefas até textos. O software gerenciador de filas armazena as mensagens até que um aplicativo de recebimento se conecte e reture uma mensagem da fila. O aplicativo receptor então processa a mensagem.

<p align="center">
<img src="https://www.cloudamqp.com/img/blog/workflow-rabbitmq.png"/>
</p>

As mensagem não são publicadas diretamente em uma fila, em vez disso, o produtor envia mensagens para uma exchange. Uma exchage é reponsavel por rotear as mensagens para diferentes filas com a ajuda de bindings e routing Keys.

<p align="center">
<img src="https://www.cloudamqp.com/img/blog/exchanges-bidings-routing-keys.png"/>
</p>

Fonte: 
- https://www.cloudamqp.com/blog/part1-rabbitmq-for-beginners-what-is-rabbitmq.html
- https://www.cloudamqp.com/blog/part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html

