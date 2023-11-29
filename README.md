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

Name                Stmts   Miss  Cover
---------------------------------------
test_assembler.py      55      0   100%
test_vm.py             14      0   100%
---------------------------------------
TOTAL                  69      0   100%


You can observe that out of all lines all of them have been covered by our test script, as a result we have Cover 100% in both  `test_assembler.py ` and  `test_vm.py `. The number under the Missing column gives the line that has not been tested.
