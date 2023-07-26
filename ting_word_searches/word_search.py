def exists_word(mundo, instancia):
    lista = []
    dicionario = dict()
    dicionario["palavra"] = ""
    dicionario["arquivo"] = ""
    dicionario["ocorrencias"] = []
    contador = 1

    for x in range(0, instancia._tamanho):
        for linha in instancia._fila[x]["linhas_do_arquivo"]:
            if str(mundo).lower() in str(linha).lower():
                dicionario["palavra"] = mundo
                dicionario["arquivo"] = instancia._fila[x]["nome_do_arquivo"]
                dicionario["ocorrencias"].append({"linha": contador})
                if len(lista) == 0:
                    lista.append(dicionario)
            contador += 1
        contador = 1
    return lista


def search_by_word(mundo, instancia):
    lista = []
    dicionario = dict()
    dicionario["palavra"] = ""
    dicionario["arquivo"] = ""
    dicionario["ocorrencias"] = []
    contador = 1

    for x in range(0, instancia._tamanho):
        for linha in instancia._fila[x]["linhas_do_arquivo"]:
            if str(mundo).lower() in str(linha).lower():
                dicionario["palavra"] = mundo
                dicionario["arquivo"] = instancia._fila[x]["nome_do_arquivo"]
                dicionario["ocorrencias"].append(
                    {
                        "linha": contador,
                        "conteudo": linha
                    }
                )
                if len(lista) == 0:
                    lista.append(dicionario)
            contador += 1
        contador = 1
    return lista
