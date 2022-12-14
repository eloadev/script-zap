from message_generator import Message
from whatsapp_automation import AutomacaoZap

message = Message()
movie = message.define_message()
script_text = movie['script']
print(script_text)

automacao = AutomacaoZap(script_text)
automacao.envia_mensagem(script_text)
