def exists_word(word, instance):
    result = list()

    for data in instance.items:
        result.append(
            {
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [
                    {"linha": index + 1}
                    for index, line in enumerate(data["linhas_do_arquivo"])
                    if word.lower() in line.lower()
                ],
                "palavra": word.lower(),
            }
        )

    if not result[0]["ocorrencias"]:
        return []

    return result


def search_by_word(word, instance):
    result = list()

    for data in instance.items:
        result.append(
            {
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [
                    {
                        "linha": index + 1,
                        "conteudo": line,
                    }
                    for index, line in enumerate(data["linhas_do_arquivo"])
                    if word.lower() in line.lower()
                ],
                "palavra": word.lower(),
            }
        )

    if not result[0]["ocorrencias"]:
        return []

    return result
