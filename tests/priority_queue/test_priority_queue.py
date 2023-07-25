from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process
import pytest


def test_basic_priority_queueing():
    fila = PriorityQueue()
    process("statics/novo_paradigma_globalizado.txt", fila)
    process("statics/nome_pedro.txt", fila)
    process("statics/novo_paradigma_globalizado-min.txt", fila)
    process("statics/arquivo_teste.txt", fila)
    
    assert len(fila.high_priority) == 2
    assert len(fila.regular_priority) == 2

    fila.dequeue()

    file_one = fila.search(0)
    assert file_one["nome_do_arquivo"] == "statics/arquivo_teste.txt"

    with pytest.raises(IndexError):
        fila.search(10)
