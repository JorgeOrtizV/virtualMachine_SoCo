import subprocess
import pytest

def run_assembler(input_as, output_mx):
    cmd = [
        'python',
        'debugger/assembler.py',
        input_as,
        output_mx
    ]
    subprocess.run(cmd, check=True)

def test_addTwoNumbers():
    input_as = 'exercise 1/addTwoNumbers.as'
    output_mx = 'exercise 1/addTwoNumbers.mx'
    expected_output_mx = 'exercise 1/test_addTwoNumbers.mx'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_subtractTwoNumbers():
    input_as = 'exercise 1/subtractTwoNumbers.as'
    output_mx = 'exercise 1/subtractTwoNumbers.mx'
    expected_output_mx = 'exercise 1/test_subtractTwoNumbersmx'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output
