

class AutomacaoZap:
    def __init__(self, message):
        self.message = message

    def envia_mensagem(self, message):
        number = '+5522981474624'

        Webdriver driver = ChromeDriver()
        try:
            pywhatkit.sendwhatmsg_instantly(number, "teste", 6)
            pywhatkit.sendwhatmsg_instantly(number, "elo", 6)
            print("Success")
        except Exception:
            print("Error")


teste = AutomacaoZap("aaa")
teste.envia_mensagem("aaa")