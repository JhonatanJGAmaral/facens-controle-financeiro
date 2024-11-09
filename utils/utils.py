# esse arquivo (com a classe "Utils") funciona como uma implementação de CONTRATO,
# via INTERFACE para Python mesmo Python não tendo interface 

# from pasta.arquivo import classe
from configurations.configurations import Configurations

class Utils():
    def __init__(self):
        # isso funciona como injeção de dependências
        # Injeção de Dependências: preciso usar uma classe sem herdá-la 
        self.__config = Configurations()

    def read_file(self):
        # file_output é uma property, portanto não precisa dos parênteses (não é callable)
        with open(self.__config.file_output, 'r') as file:
            return list(map(lambda x: x.replace('\n', ''), file.readlines()))

    # como esse é um método dentro da classe, não um CONSTRUTOR (__init__)
    # pode ser que o programa reclame da variável chamada "type", pois essa 
    # palavra já está sendo usada como palavra reservada (type())
    def write_file(self, _type, value, description):
        with open(self.__config.file_output, 'a+') as file:
            file.write(f'\nOperação: {_type} - Valor: {value} - Descrição: {description}')