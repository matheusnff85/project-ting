import sys
from ting_file_management.file_management import txt_importer


def process(file_path, queue):
    files = [item["nome_do_arquivo"] for item in queue.items]

    if file_path not in files:
        file = txt_importer(file_path)
        dict_data = {
            "nome_do_arquivo": file_path,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        queue.enqueue(dict_data)
        print(dict_data, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        file = instance.dequeue()
        file_path = file["nome_do_arquivo"]
        print(f"Arquivo {file_path} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
    else:
        print(file, file=sys.stdout)
