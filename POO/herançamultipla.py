class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        else:
            print(f'{self._nome} ligando')
            self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} já está desligado')
            return
        else:
            print(f'{self._nome} desligando')
            self._ligado = False


# CLASSE PARA ADICIONAR FUNCIONALIDADES A OUTRAS
class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


# SMARTPHONE
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} está desligado'
            print(info)
            self.log_info(info)
            return
        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return
        self._conectado = True
        info = f'{self._nome} conectando'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado'
            print(error)
            self.log_error(error)
            return
        self._conectado = False
        info = f'{self._nome} desconectando'
        print(info)
        self.log_info(info)


smart = Smartphone('Xiaomi')

print()
smart.desligar()
smart.desconectar()
smart.conectar()
smart.ligar()
smart.conectar()
smart.conectar()
smart.desconectar()
smart.desligar()
