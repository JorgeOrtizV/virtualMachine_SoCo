import subprocess
import pytest
import sys
def run_assembler(input_as, output_mx):
    python_cmd = 'python'
    if sys.platform == 'win32':
        python_cmd = 'py'
    cmd = [
        python_cmd,
        '../vm/assembler.py',
        input_as,
        output_mx
    ]
    subprocess.run(cmd, check=True)

def test_addTwoNumbers():
    input_as = 'assembler_code/addTwoNumbers.as'
    output_mx = 'assembler_output/addTwoNumbers.mx'
    expected_output_mx = 'test_files/expected_addTwoNumbers.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_subtractTwoNumbers():
    input_as = 'assembler_code/subtractTwoNumbers.as'
    output_mx = 'assembler_output/subtractTwoNumbers.mx'
    expected_output_mx = 'test_files/expected_subtractTwoNumbers.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_UseOf_beq():
    input_as = 'assembler_code/UseOf_beq.as'
    output_mx = 'assembler_output/UseOf_beq.mx'
    expected_output_mx = 'test_files/expected_UseOf_beq.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_Loop():
    input_as = 'assembler_code/Loop.as'
    output_mx = 'assembler_output/Loop.mx'
    expected_output_mx = 'test_files/expected_Loop.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output

def test_memLoad():
    input_as = 'assembler_code/StoreLoadFromMemory.as'
    output_mx = 'assembler_output/StoreLoadFromMemory.mx'
    expected_output_mx = 'test_files/expected_StoreLoadFromMemory.txt'

     # Define the expected output

    run_assembler(input_as, output_mx)

    with open(output_mx, 'r') as file:
        output = file.read()
    
    with open(expected_output_mx, 'r') as file:
        expected_output = file.read()
    
    assert output == expected_output
