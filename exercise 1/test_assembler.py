import subprocess
import pytest

def run_assembler(input_as, output_mx):
    # TODO: make this robust to run in either win, linux, mac
    cmd = [
        'py',
        '../vm/assembler.py',
        input_as,
        output_mx
    ]
    subprocess.run(cmd, check=True)

def test_addTwoNumbers():
    input_as = 'addTwoNumbers.as'
    output_mx = 'addTwoNumbers.mx'
    expected_output_mx = 'test_addTwoNumbers.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_subtractTwoNumbers():
    input_as = 'subtractTwoNumbers.as'
    output_mx = 'subtractTwoNumbers.mx'
    expected_output_mx = 'test_subtractTwoNumbers.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_UseOf_beq():
    input_as = 'test_UseOf_beq.as'
    output_mx = 'test_UseOf_beq.mx'
    expected_output_mx = 'test_UseOf_beq.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_Loop():
    input_as = 'Loop.as'
    output_mx = 'Loop.mx'
    expected_output_mx = 'test_Loop.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output
