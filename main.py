from message_generator import Message
from whatsapp_automation import AutomationZap

print("## WELCOME TO THE WHATSAPP MOVIE SCRIPT SENDER ##\n")

message = Message()
movie_script = message.define_message()

contact = input("\nContact to send the message: ")

print("\nDon`t forget to SCAN the QR code and ENTER WhatsApp")

automation = AutomationZap()
automation.send_message(movie_script, contact)
