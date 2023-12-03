# virtualMachine_SoCo
## Overview
For the first exercise we have made a folder ` exercise 1`  in which we have the assemble examples `assembler code`, the tests for these examples `test_files` and the outputs of the assembler `assembler_output` and the output of vm `vm_output`. For the exercise two we have in the folder `exercise 2 ` the disassembler `disassembler.py` , its test `test_disassembler.py` and the examples. In `exercise 3` folder we have the examples and the outputs for every quetsion.

## Features
#### VIRTUAL MACHINE(VM)
-Memory Management: Simulates memory allocation, access, and management techniques used in real-world VMs.

#### Debugger
-Breakpoints: Ability to set and manage breakpoints for effective debugging.
-Step Execution: Feature to execute code step-by-step for detailed analysis.
-Variable Inspection: Tools to inspect and modify the values of variables during runtime.

#### Disassembler
-Reverse Engineering: Converts machine code back into a human-readable assembly language format
### Unit Testing
-Automated Tests: Implementation of automated tests to validate the functionality of each component.
-Test Coverage Analysis: Tools to analyze the extent of code covered by the tests to ensure thorough testing.

#### Additional Features
-User Interface: A simple, intuitive interface for interacting with the VM and debugger.
-Documentation: Comprehensive documentation for each module, detailing its purpose and usage.
-Error Handling: Robust error handling mechanisms to manage and report errors gracefully.

### Exercise 1 (B)
i) 
Not assuming the correctness of the Assembler introduces a range of complexities, from the need for extensive testing and validation to robust error handling and user communication.

### Exercise 1 (C)
In the folder `exercise 1` we have in `assembler_code` a file `outOfMemory.as` where we have implemented an example with many loops which drive the system out of memory.
```bash
py "vm\arrays.py" "exercise 1\assembler_code\outOfMemoryError.as" "exercise 1\assembler_code\outOfMemoryError.mx"
```
![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/141324290/f6bbd0de-f6f5-4e0b-9004-3201f693468b)


# Measure and Report the test coverage


### The step we use 

```bash
pip install coverage
```
```bash
coverage run -m pytest

```
```bash
coverage report
```
and it will be in the command line the report below:

![WhatsApp Image 2023-11-29 at 15 01 51_0a97da70](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/141324290/30bc3f9e-895d-44f0-b0fa-6d4f0f04f8d8)



You can observe that out of all lines all of them have been covered by our test script, as a result we have Cover 100% in both  `test_assembler.py ` and  `test_vm.py `. The number under the Missing column gives the line that has not been tested.

### How to RUN
Exercise 1 one we first run the example with the assembler:
```bash
py "vm/assembler.py" "exercise 1\assembler_code\StoreLoadFromMemory.as" "exercise 1\assembler_code\StoreLoadFromMemory.mx"
```
and next we run the output .mx file with the vm:

```bash
py "vm/vm.py" "exercise 1\assembler_code\StoreLoadFromMemory.mx" "exercise 1\assembler_code\StoreLoadFromMemory_vm.mx" 
```
The tests:
```bash
pytest "exercise 1\test_assembler.py"
```

```bash
 pytest "exercise 1\test_vm.py"
```

Exercise 2 :

```bash
py "exercise 2\disassembler.py" "exercise 2\converted_mx_as\addTwoNumbers.mx" "exercise 2\converted_mx_as\addTwoNumbers.as"
```
For the test:
```bash
 pytest "exercise 2\test_disassembler.py"
```
Exercise 3 :
we run every example like:

```bash
 py "vm\assembler.py" "exercise 3\example_3_1.as" "exercise 3\example_3_1.mx"
```
```bash
py "vm\vm.py" "exercise 3\example_3_1.mx" -
```
Exercise 4 :

Exercise 4:

## Description of the files
### 1. assembler-code 
we have all the examples of exercise 1 with assembly.
### 2. assembler-output
we have all the outputs.mx files of the assembler 
### 2. vm-output
we have all the outputs_vm.mx files of the vm 
### 3. test_files 
we have all the .txt files we use for the test









