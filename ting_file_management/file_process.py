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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
