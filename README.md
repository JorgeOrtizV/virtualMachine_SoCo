# virtualMachine_SoCo
Assignment 3 for the course Software Construction @ UZH

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
