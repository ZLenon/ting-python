from ting_file_management.file_management import txt_importer
import sys


def process(file_path, instancia):
    lista_linhas = txt_importer(file_path)
    span = {}

    span["nome_do_arquivo"] = file_path
    span["qtd_linhas"] = len(lista_linhas)
    span["linhas_do_arquivo"] = lista_linhas

    if instancia.__len__() == 0:
        instancia.enqueue(span)
        print(span, file=sys.stdout)

    arquivos = []

    for i in range(0, instancia.__len__()):
        file = instancia.search(i)
        arquivos.append(file["nome_do_arquivo"])

    if file_path not in arquivos:
        instancia.enqueue(span)
        print(span, file=sys.stdout)


def remove(instancia):
    if instancia.__len__() == 0:
        return print("Não há elementos", file=sys.stdout)

    arquivo = instancia.dequeue()
    file_path = arquivo["nome_do_arquivo"]

    return print(f"Arquivo {file_path} removido com sucesso", file=sys.stdout)


def file_metadata(instancia, posicao):
    try:
        file = instancia.search(posicao)
        return print(file, file=sys.stdout)
    except Exception:
        print("Posição inválida", file=sys.stderr)
