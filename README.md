# virtualMachine_SoCo
## Overview
This repository contains an implementation of an assembler, virtual machine, and debugger using the programming language Python. To enhance the capabilities of the Virtual Machine implementation unit testing was perfomed, a disassembler was implemented, and new features were added, such as the capability to add watchpoints or the swaping action. For the first exercise we have made a folder ` exercise 1`  in which we have the assemble examples `assembler code`, the tests for these examples `test_files` and the outputs of the assembler `assembler_output` and the output of vm `vm_output`. For the exercise two we have in the folder `exercise 2 ` the disassembler `disassembler.py` , its test `test_disassembler.py` and the examples. In `exercise 3` folder we have the examples and the outputs for every quetsion.

## Features
#### VIRTUAL MACHINE(VM)
- Memory Management: Simulates memory allocation, access, and management techniques used in real-world VMs.

#### Debugger
- Breakpoints: Ability to set and manage breakpoints for effective debugging.
- Step Execution: Feature to execute code step-by-step for detailed analysis.
- Variable Inspection: Tools to inspect and modify the values of variables during runtime.

#### Disassembler
- Reverse Engineering: Converts machine code back into a human-readable assembly language format
### Unit Testing
- Automated Tests: Implementation of automated tests to validate the functionality of each component.
- Test Coverage Analysis: Tools to analyze the extent of code covered by the tests to ensure thorough testing.

#### Additional Features
- User Interface: A simple, intuitive interface for interacting with the VM and debugger.
- Documentation: Comprehensive documentation for each module, detailing its purpose and usage.
- Error Handling: Robust error handling mechanisms to manage and report errors gracefully.

### Exercise 1 (A)
Unit Tests were developed to test each of the existing functionalities of our assembler and virtual machine. The assembler codes can be found in the folder `assembler_code`, the outputs of the assembler are stored in the folder `assembler_output`, and the results of the virtual machine in `vm_output`. Files relevant for the module pytest are stored in the folder `test_files`. To run the tests of this section it is only necessary to change directory to the folder `exercise 1` and run the command `pytest`. In the `test_files` it is possible to find the expected output of the test files. This output was calculated by hand based on the assembler code.

### Exercise 1 (B)
i) What are the implications of not assuming that the assembler is correct? 
Not assuming the correctness of the Assembler introduces a range of complexities, from the need for extensive testing and validation to robust error handling and user communication.

### Exercise 1 (C)
In the folder `exercise 1`, The file to test the Out Of Memory Error can be found in `assembler_code/outOfMemoryError.as` and the file to test the no instruction is found in `assembler_output/noInstruction.mx`

```bash
pytest
```
![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/141324290/f6bbd0de-f6f5-4e0b-9004-3201f693468b)
![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/138753fa-c52f-4fc4-9c14-7c19c3c03498)

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
py "vm/assembler.py" "exercise 1\assembler_code\StoreLoadFromMemory.as" "exercise 1\assembler_output\StoreLoadFromMemory.mx"
```
and next we run the output .mx file with the vm:

```bash
py "vm/vm.py" "exercise 1\assembler_output\StoreLoadFromMemory.mx" "exercise 1\vm_output\StoreLoadFromMemory_vm.mx" 
```
To run the tests it is only necessary to run the command
```bash
pytest 
```

### Exercise 2 :
For this section a disassembler was programmed using python. The code for the disassembler acn be found in `disassembler.py` and the test of the module in `test_disassembler.py`

Execution:
```bash
py "exercise 2\disassembler.py" "exercise 1\assembler_output\addTwoNumbers.mx" "exercise 2\converted_mx_as\addTwoNumbers.as"
```
As it is possible to observe, an .mx file produced by the working assembler was taken and the translation was obtained by the disassembler. The test module compares that this produced file is exactly the same as the one used on exercise 1 to obtain the .mx file.

For testing cbange directory to exercise 2 and run:
```bash
pytest
```
![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/2d6c27df-58cd-47c2-89c3-88908ddc4852)

### Exercise 3 :
For the exercise 3, the increase, decrease, and swap functionalities were added to the assembler and virtual machine. Additionally tests for each function were created, including an assembler code to reverse arrays on place. Not that for this to work it is necessary to execute it with the enhanced code `arrays.py` instead of `assembler.py`

we run every example like:

```bash
 py "vm\assembler.py" "exercise 3\example_3_1.as" "exercise 3\example_3_1.mx"
```
```bash
py "vm\vm.py" "exercise 3\example_3_1.mx" -
```

The following screenshot demonstrate the correct functionality of the reversing arrays inplace implementation. Where the array was implemented to contain numbers from 1 to 6 (printed through the vm) and after reversing the same array shows the same items in reversed order.

![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/107a2f6a-114c-4b7f-b9f5-0f976369a3d9)


### Exercise 4:
##### Display specific memory addresses
If the user execute the debugger script `vm_extend.py` or `vm_break.py` the user is able to run the debugging command `m` or `memory` to display all the memory addresses, `m A` to get a specific memory address or `m A B` to display all the memories in between A and B, where A and B are integers representing memory addresses.

![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/c6a5a1cc-5465-4e3e-ae28-0b6cd9dd13a2)

##### Add break and clear features
The user can provide the command `b` or `break` to add a breakpoint and `c` or `clear` to remove an existing breakpoint. If the breakpoint command is used to an already existing breakpoint instruction or clear is applied to a non-breakpoint instruction no change is made to the existing instructions.

![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/d0bce780-ce2e-47ce-9dd9-9b9bea7fe1db)

##### Command Completion
If the user gives a part of the command but not exactly the existing command, the program figures out which command the user wants to execute based on similarity. For example, `mem` would run `memory` actions. This is only achievable when the given string of the user matches only one command. If more than a command is matched a list of suggestions are returned to the user. This to avoid executing undesired actions.

![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/1ff17270-5f9f-4899-8f5a-764282647200)

##### Adding watchpoints
The user is able to use the commands `w` or `watchpoint` plus a memory address to set a watchpoint to the given memory address. In the case that the content of the memory address change the program will automatically halt enabling the user to execute further debugging instructions for analysis. To test this functionality an extra test was developed `vm/testWatchpoint.mx`

![image](https://github.com/JorgeOrtizV/virtualMachine_SoCo/assets/62453342/7a5cf3cb-031b-499e-b688-b24aae80e54a)

## Description of the files
### test_assembler.py
We have implemented the tests for each example for the assembler.
### test_vm.py
We have implemented the tests for each example for the vm.

### disassembler.py
We have implemented the disassembler, which takes the mx.file and outputs the initial .as file, which is readable by the user.

### test_disassembler.py
We have implemented the test for each example we have and we run it with the use of pytest.

For exercise 3, we don't have new files we expanded the `architecture.py` by 3 more instructions: `inc` `dec` and `swp` and we modify the rest files.

### debugger
- vm_base.py : Include the base functionalities of the virtual machine.
- vm_extend.py : Add debugging functionalities to the virtual machine.
- vm_step.py : Enables stepping through all the instructions.
- vm_break.py : Enable the ussage of breakpoints.







