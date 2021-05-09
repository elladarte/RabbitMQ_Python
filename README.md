# RabbitMQ

## Introdução

É um software de enfilerameto de mensagens também conhecidos como intermediario de mensagens ou gerenciador de filas.
Uma mensagem pode incluir qualquer tipo de informação, dede de processos de tarefas até textos. O software gerenciador de filas armazena as mensagens até que um aplicativo de recebimento se conecte e reture uma mensagem da fila. O aplicativo receptor então processa a mensagem.


As mensagem não são publicadas diretamente em uma fila, em vez disso, o produtor envia mensagens para uma exchange. Uma exchage é reponsavel por rotear as mensagens para diferentes filas com a ajuda de bindings e routing Keys.
