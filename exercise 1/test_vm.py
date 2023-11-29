import subprocess
import pytest
def run_array(input_as):
    # TODO: make this robust to run in either win, linux, mac
    cmd = [
        'py',
        '../vm/arrays.py',
        input_as,
        'test_files/test_OOMError.mx'
    ]
    subprocess.run(cmd, check=True)

def run_vm(input_as):
    # TODO: make this robust to run in either win, linux, mac
    cmd = [
        'py',
        '../vm/vm.py',
        input_as,
        'test_files/noInstruction_vm.mx'
    ]
    subprocess.run(cmd, check=True)


def test_outOfMemoryError():
    input_as = 'assembler_code/outOfMemoryError.as'
    run_array(input_as)


def test_nonExistingInstruction():
    input_as = 'assembler_output/noInstruction.mx'
    run_vm(input_as)
    
