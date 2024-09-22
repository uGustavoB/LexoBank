class ContaInexistenteError(Exception):
    def __init__(self, codigoError, msg):
        super().__init__(msg)
        self.codigoError = codigoError