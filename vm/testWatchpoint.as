# Adding memory allocation to this script to test watchpoints

# Count up to 3.
# - R0: loop index.
# - R1: loop limit.
ldc R0 0
ldc R3 20
str R0 R3
hlt
