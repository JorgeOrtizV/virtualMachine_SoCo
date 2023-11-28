import subprocess
import pytest
def run_array(input_as):
    # TODO: make this robust to run in either win, linux, mac
    cmd = [
        'py',
        'vm/arrays.py',
        input_as,
    #    output_mx
    ]
    subprocess.run(cmd, check=True)

def test_outOfMemoryError():
    input_as = 'outOfMemoryError.as'
    #output_mx='outOfMemoryError.mx'
    run_array(input_as)
    
    # # Define the expected output
    # expected_output_mx = 'expected_output_mx.mx'


    #run_array(input_as, output_mx)

    # with open(output_mx, 'r') as file:
    #     output = file.read()
    
    # with open(expected_output_mx, 'r') as file:
    #     expected_output = file.read()
    
    # assert output == expected_output
