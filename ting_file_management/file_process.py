import sys


def process(file_path, instancia):
    """Aqui irá sua implementação"""


def remove(instancia):
    if instancia.__len__() == 0:
        return print("Não há elementos", file=sys.stdout)

    arquivo = instancia.dequeue()
    path_file = arquivo["nome_do_arquivo"]

    return print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instancia, posicao):
    """Aqui irá sua implementação"""
