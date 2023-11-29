# memory spaces
ldc R0 10
ldc R1 11
# values
ldc R2 1
ldc R3 2
# Load values
str R2 R0
str R3 R1
#Swap content in R0 and R1
swp R0 R1
# See that R0 is 2 and R1 is 1
prm R0
prm R1
hlt
