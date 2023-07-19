# sys é um módulo embutido em Python que fornece acesso recursos relacionados
# ao sistema. O stderr é um objeto de fluxo de saída de erros.
import sys


# Função para importar um arquivo de texto
def txt_importer(path_file):
    # Verifica se o caminho do arquivo não possui a extensão .txt
    # endswith verificar se uma string termina com um determinado sufixo
    if not str(path_file).endswith(".txt"):
        # Retorna uma mensagem de formato inválido 
        # para a saída de erros padrãos
        return print("Formato inválido", file=sys.stderr)

    # Lista vazia para armazenar as linhas do arquivo
    lista = []

    try:
        # Abre o arquivo no caminho especificado
        with open(path_file) as file:
            # Itera sobre as linhas do arquivo
            for linha in file:
                # Adiciona a linha à lista de linhas, 
                # removendo espaços em branco no início e no fim
                lista.append(linha.strip())
        # Retorna a lista de linhas do arquivo
        return lista
    except Exception:
        # Retorna uma mensagem de arquivo não encontrado 
        # para a saída de erros padrão
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
