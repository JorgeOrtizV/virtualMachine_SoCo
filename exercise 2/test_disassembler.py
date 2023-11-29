import subprocess
import pytest
import sys
def run_disassembler(input_mx, output_as):
    python_cmd = 'python'
    if sys.platform == 'win32':
        python_cmd = 'py'

    cmd = [
        python_cmd,
        '../exercise 2/disassembler.py',
        input_mx,
        output_as
    ]
    subprocess.run(cmd, check=True)

def test_disassembler_addTwoNumbers():
    testing='addTwoNumbers'
    expected_as = f'../exercise 1/assembler_code/{testing}.as'
    input_mx = f'../exercise 1/assembler_output/{testing}.mx'
    output_as= f'../exercise 2/converted_mx_as/{testing}.as'
    run_disassembler(input_mx, output_as)

    with open(expected_as, 'r') as f1, open(expected_as, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        assert content1 == content2, "as files are not the same"


def test_disassembler_Loop():
    testing='Loop'
    expected_as = f'../exercise 1/assembler_code/{testing}.as'
    input_mx = f'../exercise 1/assembler_output/{testing}.mx'
    output_as= f'../exercise 2/converted_mx_as/{testing}.as'
    run_disassembler(input_mx, output_as)

    with open(expected_as, 'r') as f1, open(expected_as, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        assert content1 == content2, "as files are not the same"

def test_disassembler_subtractTwoNumbers():
    testing='subtractTwoNumbers'
    expected_as = f'../exercise 1/assembler_code/{testing}.as'
    input_mx = f'../exercise 1/assembler_output/{testing}.mx'
    output_as= f'../exercise 2/converted_mx_as/{testing}.as'
    run_disassembler(input_mx, output_as)

    with open(expected_as, 'r') as f1, open(expected_as, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        assert content1 == content2, "as files are not the same"

